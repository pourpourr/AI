import string

NAME="2-f24"


def readFiles():
    print(NAME)
    v = open("var"+NAME+".txt", "r")
    d = open("dom"+NAME+".txt","r")
    c = open("ctr"+NAME+".txt","r")

    constraint_lines = c.readlines()
    numOfconstraints= int(constraint_lines[0])
    neighbors={}

    for i in range(1,numOfconstraints+1):
        stuff= constraint_lines[i].split()
        if int(stuff[0]) not in neighbors:
            neighbors[int(stuff[0])]=[]
        neighbors[int(stuff[0])].append(int(stuff[1]))  # 0 is neighbor of 1
        if int(stuff[1]) not in neighbors:
            neighbors[int(stuff[1])]=[]
        neighbors[int(stuff[1])].append(int(stuff[0]))   # 1 is neighbor of 0
    domain_lines = d.readlines()
    variable_lines = v.readlines()
    numOfvars= int(variable_lines[0])

    domains={}
    variables=[]
    for i in range(1,numOfvars+1):
        variables.append(i-1)
        var_line= variable_lines[i].split()
        dom_line= domain_lines[int(var_line[1])+1].split()
        currDom=[]
        for j in range(0,int(dom_line[1])):
            currDom.append(int(dom_line[j+2]))
        domains[int(var_line[0])]=list(currDom)

    u=tuple((variables,domains, neighbors))
    return u
