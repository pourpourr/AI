import CSP

NAME="2-f24"

constCount=0
constraints_dict={}


def constraints(A,a,B,b):
    global constCount
    if len(constraints_dict)==0:

        c = open("ctr"+NAME+".txt","r")

        constraint_lines = c.readlines()

        numOfconstraints= int(constraint_lines[0])


        for i in range(1,numOfconstraints+1):
            stuff= constraint_lines[i].split()
            constraints_dict[stuff[0]+','+stuff[1]]=[]
            constraints_dict[stuff[0]+','+stuff[1]].append(stuff[2])
            constraints_dict[stuff[0]+','+stuff[1]].append(int(stuff[3]))
            constraints_dict[stuff[1]+','+stuff[0]]=[]
            constraints_dict[stuff[1]+','+stuff[0]].append(stuff[2])
            constraints_dict[stuff[1]+','+stuff[0]].append(int(stuff[3]))
    u=str(A)+','+str(B)
    constCount+=1
    if u in constraints_dict:
        result=constraints_dict[u]
        if result[0]=='=':
            return abs(int(a)-int(b))==result[1]
        else:
            return abs(int(a)-int(b))>result[1]
    return True



def wdeg(assignment, csp, weight):
    max=-1
    maxVar= None
    for var in csp.variables:
        s=0
        if var not in assignment:
            for b in csp.neighbors[var]:
                if b not in assignment:
                    s= s+ weight[var,b]
        if s>max:
            max=s
            maxVar=var
    if not maxVar:
        for v in csp.variables:
            if v not in assignment:
                return v
    return maxVar

def dom_wdeg(assignment, csp, weight):
    min=100000000000000000
    minVar= None
    for var in csp.variables:
        s=0
        if var not in assignment:
            for b in csp.neighbors[var]:
                if b not in assignment:
                    s= s+ weight[var,b]
        if s>0:
            if csp.curr_domains is not None:
                    s=len(csp.curr_domains[var])/s
            else:
                    s=len(csp.domains[var])/s

        if s<min and s>0:
            min=s
            minVar=var
    if not minVar:
        for v in csp.variables:
            if v not in assignment:
                return v
    return minVar



def forward_checking(csp, var, value, assignment, removals, weight):
    """Prune neighbor values inconsistent with var=value."""
    csp.support_pruning()
    for B in csp.neighbors[var]:
        if B not in assignment:
            for b in csp.curr_domains[B][:]:
                if not csp.constraints(var, value, B, b):
                    csp.prune(B, b, removals)
            if not csp.curr_domains[B]:
                weight[var, B]+=1
                weight[B, var]+=1
                return False,weight
    return True,weight

def AC3(csp,weight, queue=None, removals=None, arc_heuristic=CSP.dom_j_up  ):
    """[Figure 6.3]"""
    if queue is None:
        queue = {(Xi, Xk) for Xi in csp.variables for Xk in csp.neighbors[Xi]}
    csp.support_pruning()
    queue = arc_heuristic(csp, queue)
    checks = 0
    while queue:
        (Xi, Xj) = queue.pop()
        revised, checks = CSP.revise(csp, Xi, Xj, removals, checks)
        if revised:
            if not csp.curr_domains[Xi]:
                weight[Xi,Xj]+=1
                weight[Xj,Xi]+=1
                return False, weight  # CSP is inconsistent
            for Xk in csp.neighbors[Xi]:
                if Xk != Xj:
                    queue.add((Xk, Xi))
    return True,  weight  # CSP is satisfiable




def mac(csp, var, value, assignment, removals,weight, constraint_propagation=AC3):
    """Maintain arc consistency."""
    return constraint_propagation(csp,weight, {(X, var) for X in csp.neighbors[var]}, removals)


def backtracking_search(csp, select_unassigned_variable,
                        order_domain_values, inference):
    """[Figure 6.5]"""
    weight={}
    for var in csp.variables:
        for neigh in csp.neighbors[var]:
            weight[var, neigh]=1
    global nodesCount
    nodesCount=0
    global constCount
    constCount=0

    def backtrack(assignment , weight):

        global nodesCount
        if len(assignment) == len(csp.variables):
            return assignment

        var = select_unassigned_variable(assignment, csp, weight)
        for value in order_domain_values(var, assignment, csp ):
            if 0 == csp.nconflicts(var, value, assignment):
                csp.assign(var, value, assignment)
                nodesCount+=1

                removals = csp.suppose(var, value)
                solution,weight=inference(csp, var, value, assignment, removals,weight)
                if solution:
                    result = backtrack(assignment, weight)
                    if result is not None:
                        return result
                csp.restore(removals)
        csp.unassign(var, assignment)
        return None

    result = backtrack({},weight)
    assert result is None or csp.goal_test(result)

    return result,nodesCount,constCount
