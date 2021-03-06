import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import CountVectorizer

data_dict = dict()

# 用于处理训练用的csv数据
def data_process(file, feature_list, data_dict):
    target = pd.read_csv('phase2/trace2_test/'+file+'.csv',encoding='utf-8')

    x_list = []
    for j in range(len(feature_list)):
        x_list.append(target.get(feature_list[j]))

    x_sha1 = target.get('sha1')

    for i in range(len(x_sha1)):
        if x_sha1[i] not in data_dict.keys():
            data_dict[x_sha1[i]] = \
                {'site': '',
                 'ip': '',
                 'domain': '',
                 'register_username': '',
                 'email_address': '',
                 'email': '',
                 'phone_number': '',
                 'url': ''
                 }
            for j in range(len(feature_list)):
                data_dict[x_sha1[i]][feature_list[j]] = [str(x_list[j][i])]
        else:
            for j in range(len(feature_list)):
                if data_dict[x_sha1[i]][feature_list[j]]:
                    data_dict[x_sha1[i]][feature_list[j]] = data_dict[x_sha1[i]][feature_list[j]] \
                                                        + [str(x_list[j][i])]
                else:
                    data_dict[x_sha1[i]][feature_list[j]] = [str(x_list[j][i])]
            # data_dict[x_sha1[i]]['ip'] = data_dict[x_sha1[i]]['ip'] + [x_ip[i]]

    # print(len(data_dict))

    return data_dict

# 用于保存数据处理结果
def save_csv(data_dict):
    site_list, ip_list, domain_list, register_username_list, email_address_list, contain_email_list, phone_number_list, url_list = [], [], [], [], [], [], [], []
    sha1_list = []
    count_num = 0
    for k in data_dict.keys():
        sha1_list.append(k)
        site_list.append(data_dict[k]['site'])
        ip_list.append(data_dict[k]['ip'])
        domain_list.append(data_dict[k]['domain'])
        register_username_list.append(data_dict[k]['register_username'])
        email_address_list.append(data_dict[k]['email_address'])
        contain_email_list.append(data_dict[k]['email'])
        phone_number_list.append(data_dict[k]['phone_number'])
        url_list.append(data_dict[k]['url'])

    dataframe = pd.DataFrame({
        'site': site_list,
        'ip': ip_list,
        'domain': domain_list,
        'register_username': register_username_list,
        'email_address': email_address_list,
        'contain_email': contain_email_list,
        'phone_number': phone_number_list,
        'url': url_list,
        'sha1': sha1_list})

    columns = ['sha1', 'site', 'ip', 'domain', 'register_username', 'email_address', 'contain_email', 'phone_number',
               'url']

    dataframe.to_csv("trace2/results/trace2-step1.csv", index=False, sep=",", encoding="utf_8_sig", columns=columns)


data_dict = data_process('fqdn_ip',['site','ip'],data_dict)
data_dict = data_process('fqdn_reginfo',['domain','register_username','email_address'],data_dict)
data_dict = data_process('trojan_email',['email'],data_dict)
data_dict = data_process('trojan_web',['url'],data_dict)
data_dict = data_process('trojan_phone',['phone_number'],data_dict)


for i in data_dict.keys():
    print(data_dict[i])

print(len(data_dict))


save_csv(data_dict)



# Vec_site=CountVectorizer(decode_error='ignore',token_pattern=r'\w',min_df=1)
# Vec_ip=CountVectorizer(ngram_range=(3,3),decode_error='ignore',token_pattern=r'\w',min_df=1)
# Vec_sha1=CountVectorizer()
#
# Vec_site.fit(x_site)
# Vec_ip.fit(x_ip)
# Vec_sha1.fit(x_sha1)
#
#
#
# x_site_vec=Vec_site.transform(x_site)
# x_ip_vec=Vec_ip.transform(x_ip)
# x_sha1_vec=Vec_sha1.transform(x_sha1)
#
# print(x_ip_vec.toarray())
# print('labels is ok?=')
#
# #x_samples=[x_sha1_vec.toarray(),x_site_vec.toarray(),x_ip_vec.toarray()]
# #x_samples=[x_sha1_vec,x_site_vec,x_ip_vec]
# #x=StandardScaler().fit(x_samples)
# tsne=TSNE(learning_rate=100)
# x=tsne.fit_transform(x_ip_vec.toarray())
# db=DBSCAN(eps=10,min_samples=10,metric='hamming').fit(x)
#
#
# labels=db.labels_
# df=pd.DataFrame(labels)
# df.to_csv('ip_clu.csv',sep=',',header=True,index=True)
#
# print('ok!')