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
PRankH = TIntFltH()
GetPageRank(G, PRankH) 
pagerank = [(key, PRankH[key]) for key in PRankH]
pagerank = sorted(pagerank, key=lambda x:-x[1])
end = time.clock()

idn=[nid for (nid, deg) in pagerank[:]]

S=[]            
Influence=[]    
R=1000
k=50
p=0.05

for i in range(k+1):
    temp=0
    for j in range(1,R+1):
        G = LoadEdgeList(PUNGraph, "edges.txt", 0, 1)
        deleteEdge(G,p)
        ListSReach=BFS(G,S)
        temp=temp+len(ListSReach)            
    Influence.append(temp/R)
    S.append(idn[i])
    
print Influence


ff=open("Pagerank Results.txt","w+")
for i in range(k+1):
    print>>ff,Influence[i]
print>>ff,"Max number of seeds : ",k
print>>ff,"Round : ",R
print>>ff,"Probability : ",p
print>>ff,"Pagerank Time : ",(end-start)," s"

ff.close()
