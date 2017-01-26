import time
import random
import string
from snap import *

G = LoadEdgeList(PUNGraph, "edges.txt", 0, 1)

SCC = GetMxScc(G)
with open("datamining_author_topics.dat") as f:
    rows = [l.strip().split('\t') for l in f]
    rows = rows[1:]
    authors_map =[t[0][0:] for t in rows]

fileC=open("Centrality Analysis Results.txt","w+")

####### Degree #######
start1 = time.clock()
degCentr = [(n.GetId(), GetDegreeCentr(G, n.GetId())) for n in G.Nodes()]
end1 = time.clock()
degCentr = sorted(degCentr, key=lambda x:-x[1])

print>>fileC, "Top 10 authors by degree centrality"
for (nid, deg) in degCentr[:10]:
    print>>fileC,authors_map[nid],'\t',deg

print>>fileC, "Time: ",(end1 - start1),"s"
print>>fileC,  "---------------------------------------------------------------"



###### Betweenness #######
start2 = time.clock()
Node_map = TIntFltH()
Edge_map = TIntPrFltH()
GetBetweennessCentr(G, Node_map, Edge_map, 1)
betwCentr = [(n.GetId(), Node_map[n.GetId()]) for n in G.Nodes()]
end2 = time.clock()
betwCentr = sorted(betwCentr, key=lambda x:-x[1])

print>>fileC, "Top 10 authors by betweenness centrality"
for (nid, betw) in betwCentr[:10]:
    print>>fileC,authors_map[nid],'\t',betw

print>>fileC, "Time: ",(end2 - start2),"s"
print>>fileC,  "---------------------------------------------------------------"




###### Closeness #######
start3 = time.clock()
closeCentr = [(n.GetId(), GetClosenessCentr(G, n.GetId())) for n in SCC.Nodes()]
end3 = time.clock()
closeCentr = sorted(closeCentr, key=lambda x:-x[1])

print>>fileC, "Top 10 authors by closeness centrality"
for (nid, close) in closeCentr[:10]:
    print>>fileC,authors_map[nid],'\t',close

print>>fileC, "Time: ",(end3 - start3),"s"
print>>fileC,  "---------------------------------------------------------------"




####### Pagerank #######
start4 = time.clock()
PRankH = TIntFltH()
GetPageRank(G, PRankH) 
pagerank = [(key, PRankH[key]) for key in PRankH]
end4 = time.clock()

pagerank = sorted(pagerank, key=lambda x:-x[1])
p=[nid for (nid, vote) in pagerank[:]]
print>>fileC, "Top 10 authors by pagerank"
for (nid, vote) in pagerank[:10]:
    print>>fileC,authors_map[nid],'\t',vote,'\t',dd[d.index(nid)],'\t',bb[b.index(nid)],'\t',cc[c.index(nid)]

print>>fileC, "Time: ",(end4 - start4),"s"

fileC.close()
