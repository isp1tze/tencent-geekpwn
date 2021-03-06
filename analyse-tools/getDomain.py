import urllib.parse
import numpy as np
from sklearn.cluster import DBSCAN
import re
import pandas as pd

def _2ldCheck(adj,target):
    num=0
    for i in target:
        if adj == i:
            num=num+1

    return num
#^\w+.
target=pd.read_csv('shortRestore_now.csv',encoding='utf-8',low_memory=False)
sha1_temp=target.get('sha1')
urls_temp=target.get('url')

sha1s=[]
urls=[]
urls_lib=[]

hosts=[]
funcs=[]

for i in urls_temp:
    urls.append(urllib.parse.unquote(i))
for i in sha1_temp:
    sha1s.append(i)

for url in urls:
    proto, rest = urllib.parse.splittype(url)
    (host,zui)= urllib.parse.splithost(rest)
    if hosts==np.nan:
        print(hosts)
    host=str(host)
    if (_2ldCheck('.', host) == 2):
        res = re.search('^\w+.', host)
        print(host + '--------->>>' + res.group(0))
        host=host.replace(res.group(0), '')
    hosts.append(host)

for i,j in zip(sha1s,hosts):
    funcs.append(i+';'+j)
funcs=set(funcs)
funcs=list(funcs)

sha1s=[]
hosts=[]

for i in funcs:
    sha1,host=i.split(';')
    sha1s.append(sha1)
    hosts.append(host)

dataframe = pd.DataFrame({
    "sha1": sha1s,
    "host": hosts
                          })
dataframe.to_csv("samples.csv", index=False, sep=",",encoding='utf_8_sig')