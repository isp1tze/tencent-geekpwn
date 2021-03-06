import pandas as pd
import re

target = pd.read_csv('trace2/results/trace2-step2.csv',encoding='utf_8_sig')

target = target.fillna('NaN')

phone_number = target.get('phone_number')
email = target.get('contain_email')
sha1 = target.get('sha1')
url = target.get('url1')
domain = target.get('domain')

dict1 = dict()
for i in range(len(url)):
    dict1[sha1[i]] = [url[i],email[i],phone_number[i],domain[i]]

target1 = pd.read_csv('trace2/results/trace2-step3.csv',encoding='utf_8_sig')

target1 = target1.fillna('NaN')

sha11 = target1.get('sha1')
id1 = target1.get('id')

dict2 = dict()
count = 0
list_sha1,list_url, list_email, list_phone,list_domain,list_ip = [],[],[],[],[],[]

# 提取类别异常庞大的类别的数据存入csv
for i in range(len(url)):
    if id1[i] == 33:
        count += 1
        list_sha1.append(sha11[i])
        list_url.append(dict1[sha1[i]][0])
        list_email.append(dict1[sha1[i]][1])
        # print(dict1[sha1[i]][3])
        list_phone.append(dict1[sha1[i]][2])
        list_domain.append(dict1[sha1[i]][3])
        # if (sha11[i], dict1[sha1[i]][3]) in dict_domain_ip.keys():
        #     list_ip.append(dict_domain_ip[[sha11[i], dict1[sha1[i]][3]]])
        #     print("YES")
        # else:
        #     print((sha11[i], dict1[sha1[i]][3]))
        #     list_ip.append(None)
        # dict2[sha1[i]] = id1[i]trace2-4.py
        # tmp = eval(dict1[sha1[i]])
        # for j in range(len(tmp)):
        #     list_final.append()

print(len(list_phone))
dataframe = pd.DataFrame({"sha1":list_sha1,
                          "url": list_url,
                          "email":list_email,
                          "phone":list_phone,
                          "domain":list_domain})


dataframe.to_csv("trace2/results/trace2-step4.csv",index=False,sep=",",encoding='utf_8_sig')


