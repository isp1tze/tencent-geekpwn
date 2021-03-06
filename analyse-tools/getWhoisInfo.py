import dns.resolver
import pandas as pd
import whois

#
# target = pd.read_csv('samples.csv')
# sha1s=target.get('sha1')
# domains=target.get('host')
# ips=[]
# domains_=[]
# num=0
# len=str(len(domains))
#
#
# domain = input("请输入域名地址： ")
# for domain in domains:
#     temp=[]
#     try:
#         A = dns.resolver.query(domain,'A')
#         for i in A.response.answer:
#             # print(i)
#             for j in i.items:
#                 temp.append(j)
#         ips.append(temp)
#         print(str(num)+'/'+len+':'+str(temp))
#     except:
#         ips.append('None')
#         print(str(num) + '/' + len + ':' + 'No result!')
#     num=num+1
#     domains_.append(domain)
#
# dataframe = pd.DataFrame({    "sha1":sha1s,
#                               "domain": domains,
#                               "ip": ips})
# dataframe.to_csv("domain.csv", index=False, sep=",")



target = pd.read_csv('domain.csv')
domains=target.get('domain')
ips=target.get('ip')
whois_domain_name=[]
whois_registrar=[]
whois_emails=[]
domains_=[]
num=0
len=str(len(domains))

for domain in domains:
    try:
        #A = dns.resolver.query(domain,'A')
        A=whois.whois(domain)
        whois_domain_name.append(A.get('domain_name'))
        whois_registrar.append(A.get('registrar'))
        whois_emails.append(A.get('emails'))
        print(str(num)+'/'+len+':'+str(A))
    except:
        whois_domain_name.append(A.get(''))
        whois_registrar.append(A.get(''))
        whois_emails.append(A.get(''))
        print(str(num) + '/' + len + ':' + 'No result!')
    num=num+1
    domains_.append(domain)

dataframe = pd.DataFrame({"domain": domains,
                          "ip": ips,
                          "whois_domain_name":whois_domain_name,
                          "whois_registrar":whois_registrar,
                          "whois_emails":whois_emails})
dataframe.to_csv("domain.csv", index=False, sep=",")