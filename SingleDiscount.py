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
n=G.GetNodes()

start = time.clock()
degCentr = [(n.GetId(), n.GetDeg()) for n in G.Nodes()]
degCentr = sorted(degCentr, key=lambda x:x[0])

idn=[nid for (nid, deg) in degCentr[:]]
degg=[deg for (nid, deg) in degCentr[:]]

d=[0]*nnode
for i in range(len(idn)):
    d[idn[i]]=degg[i]

dd=d[:]
t=[0]*nnode

S=[]
Influence=[]    
R=1000
k=50
p=0.05

G = LoadEdgeList(PUNGraph, "edges.txt", 0, 1)
for i in range(k+1):
    max_temp=0
    max_id=0
    for jj in range(nnode):
        if jj not in S:
            if dd[jj]>max_temp:
                max_temp=dd[jj]
                max_id=jj
    S.append(max_id)

    neighbor=[]
    for EI in G.Edges():
        if (EI.GetSrcNId()==max_id)|(EI.GetDstNId()==max_id):
            if EI.GetSrcNId() not in neighbor:
                neighbor.append(EI.GetSrcNId())
            if EI.GetDstNId() not in neighbor:
                neighbor.append(EI.GetDstNId())
    for jj in neighbor:
        if (jj!=max_id)&(jj not in S):
            t[jj]=t[jj]+1
            dd[jj]=d[jj]-1
    
end = time.clock()

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
ff=open("SingleDiscount Results.txt","w+")
for i in range(k+1):
    print>>ff,Influence[i]
print>>ff,"Max number of seeds : ",k
print>>ff,"Round : ",R
print>>ff,"Probability : ",p
print>>ff,"SingleDiscount Time : ",(end-start)," s"

ff.close()
