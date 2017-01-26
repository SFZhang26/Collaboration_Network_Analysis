import random
import string
from snap import *

with open("datamining_author_topics.dat") as f:
    rows = [l.strip().split('\t') for l in f]
    rows = rows[1:]
    authors_map =[t[0][0:] for t in rows]

ff=open("authors.txt","w+")
print>>ff,authors_map
ff.close()


ee=open("edges.txt","w+")

with open("datamining_coauthor_info.dat") as f:
    rows = [l.strip().split('\t') for l in f]
    rows = rows[1:]
    for t in rows:
        print>>ee,authors_map.index(t[0][0:]),'\t',authors_map.index(t[1][0:])
    
ee.close()
