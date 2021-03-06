from simHash import simhash
import pandas as pd
import urllib.parse
import re
import Levenshtein
turn=0

def countHanmingDis(A,B):
    a=simhash(A)
    b=simhash(B)
    dis=a.hammingDis(b)
    #print(dis)
    return dis

def loadContent(adj):
    temp=[]
    for i in adj:
        temp.append(i)
    temp=set(temp)
    temp=list(temp)
    return temp

def chooseCate(adj):
    target=adj[0]
    cate=[]
    delete=[]
    for index in range(len(adj)):
        if(adj[index]!=target):
            dis=countHanmingDis(adj[index],target)
            if(int(dis)<20):
                cate.append(adj[index])
                #adj.pop(index)
                delete.append(adj[index])
                print(index)
            else:
                continue
        else:
            cate.append(adj[index])
            delete.append(adj[index])
            #adj.pop(index)
    for i in delete:
        adj.remove(i)
    return cate

res=re.search(r'^\w+\.','www.vnbfgh.com')

domianA='/08'
domianB='/013'
print(Levenshtein.distance(domianA,domianB))
#print(Levenshtein.hamming(domianA,domianB))
print(Levenshtein.ratio(domianA,domianB))
print(Levenshtein.jaro(domianA,domianB))
print(Levenshtein.jaro_winkler(domianA,domianB))

print(res.group(0))