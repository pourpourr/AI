import fileRead
import CSP
import ai3
import time

(variables,domains, neighbors)=fileRead.readFiles()


FC_time=0
nodesCount=0
constCount=0
for i in range(0,3):
    problem= CSP.CSP(variables, domains, neighbors, ai3.constraints)
    start=time.time()
    result,n,c=ai3.backtracking_search(problem ,ai3.dom_wdeg,CSP.lcv,ai3.forward_checking)
    end=time.time()
    nodesCount+=n
    constCount+=c
    FC_time+=end-start

print("===FC===")
print("average time = ", FC_time/3)
print("average num of nodes expanded ",int(nodesCount/3))
print("average num of constraints checked",int(constCount/3))

mac_time=0
nodesCount=0
constCount=0
for i in range(0,3):
    problem= CSP.CSP(variables, domains, neighbors, ai3.constraints)
    start=time.time()
    result,n,c=ai3.backtracking_search(problem ,ai3.dom_wdeg,CSP.lcv,ai3.mac)
    end=time.time()
    nodesCount+=n
    constCount+=c
    mac_time+=end-start


print("===mac===")
print("average time = ", mac_time/3)
print("average num of nodes expanded ",int(nodesCount/3))
print("average num of constraints checked",int(constCount/3))
