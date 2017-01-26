import time
import random
import string
from snap import *

######################function area##########################
def deleteEdge(G,p):
    del1=[]
    del2=[]
    for EI in G.Edges():
        if(random.uniform(0,1)>p):
            del1.append(EI.GetSrcNId())
            del2.append(EI.GetDstNId())
    for i in range(len(del1)):
        G.DelEdge(del1[i],del2[i])

def BFS(G,S):
    influenced=[]
    for ni in S:
        Treee=GetBfsTree(G,ni,True,False)
        for NI in Treee.Nodes():
            if NI.GetId() not in influenced:
                influenced.append(NI.GetId())
    return influenced

#############################################################

G = LoadEdgeList(PUNGraph, "edges.txt", 0, 1)
with open("datamining_author_topics.dat") as f:
    rows = [l for l in f]

nnode=len(rows)-1
S=[]        
Influence=[]    
R=1000
k=50
n=G.GetNodes()
p=0.05

start = time.clock()

for i in range(k+1):
    s=[0]*nnode
    for j in range(1,R+1):
        G = LoadEdgeList(PUNGraph, "edges.txt", 0, 1)
        deleteEdge(G,p)
        ListSReach=BFS(G,S)  #此处S为节点的id集合
        for NI in G.Nodes():
            if NI.GetId() not in ListSReach:
                s[NI.GetId()]=s[NI.GetId()]+len(BFS(G,[NI.GetId()]))
    max_temp=0
    max_id=0
    for jj in range(nnode):
        s[jj]=s[jj]/R
        if s[jj]>max_temp:
            max_temp=s[jj]
            max_id=jj

    S.append(max_id)
    #Influence.append(Influence[-1]+max_temp)

end = time.clock()
print "NewGreedy Time : ",(end-start)," s"


T=[]
for i in range(k+1):
    temp=0
    for j in range(1,R+1):
        G = LoadEdgeList(PUNGraph, "edges.txt", 0, 1)
        deleteEdge(G,p)
        ListSReach=BFS(G,T)
        temp=temp+len(ListSReach)            
    Influence.append(temp/R)
    T.append(S[i])
    
print Influence

ff=open("NewGreedy Results.txt","w+")
for i in range(k+1):
    print>>ff,Influence[i]
print>>ff,"Max number of seeds : ",k
print>>ff,"Round : ",R
print>>ff,"Probability : ",p
print>>ff,"NewGreedy Time : ",(end-start)," s"

ff.close()
