import dns.resolver
import pandas as pd

target = pd.read_csv('samples.csv')
sha1s=target.get('sha1')
domains=target.get('host')
ips=[]
domains_=[]
num=0
len=str(len(domains))
# domain = input("请输入域名地址： ")
for domain in domains:
    temp=[]
    try:
        A = dns.resolver.query(domain,'A')
        for i in A.response.answer:
            # print(i)
            for j in i.items:
                temp.append(j)
        ips.append(temp)
        print(str(num)+'/'+len+':'+str(temp))
    except:
        ips.append('None')
        print(str(num) + '/' + len + ':' + 'No result!')
    num=num+1
    domains_.append(domain)

dataframe = pd.DataFrame({    "sha1":sha1s,
                              "domain": domains,
                              "ip": ips})
dataframe.to_csv("domain.csv", index=False, sep=",")