import datetime
import math
import copy
# -*- coding: utf-8 -*-
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(nowTime)
from ultis import *

import pandas as pd

target = pd.read_csv('trace2/results/trace2-step2.csv',encoding='utf_8_sig')

# get info from csv
target = target.fillna('NaN')
phone_number = target.get('phone_number')
email = target.get('contain_email')
sha1 = target.get('sha1')
site = target.get('site')
domain = target.get('domain')
register_username = target.get('register_username')
email_address = target.get('email_address')
ip = target.get('ip')
url = target.get('url1')

data_list = []

# 将nan数据转换成[]
def change_NaN(input_list):
    for i in range(len(input_list)):
        if input_list[i] != 'NaN':
            input_list[i] = eval(input_list[i])
        else:
            input_list[i] = []
    return input_list

# 比较vector str1 前idx个数据是否相同
def compare_vec_str(vec_str1, vec_str2, idx):
    for i in range(idx):
        if vec_str1[i] != vec_str2[i]:
            return False
    return True

# 比较ip的前几个网段是否相同
def compare_ip(ip_list1, ip_list2):
    if len(ip_list1) == 0 or len(ip_list2) == 0:
        return False
    for i in range(len(ip_list1)):
        for j in range(len(ip_list2)):
            str_ip1 = str.split(ip_list1[i],'.')
            str_ip2 = str.split(ip_list2[j], '.')
            # print(str_ip1, str_ip2)
            if ip_list1[i] == ip_list2[j]:
                return True
            # if compare_vec_str(str_ip1,str_ip2,4):
            #     return True
    return False

def compare_other(list1, list2):
    if len(list1) == 0 or len(list2) == 0 or type(list1) == float \
            or list1 == "NaN" or type(list2) == float or list2 == "NaN":
        return False
    else:
        list1 = eval(list1)
        list2 = eval(list2)
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j] and list1[i] != [] and list1[i] != '' and \
                    (list1[i] in list_key):
                # print(list1[i])
                return True
    return False

# 测试特征
def feature1(list1_item, list2_item):
    if list1_item[1] == list2_item[1] and list1_item[1] in list_key:
        return True

# 测试特征
def feature(list1_item, list2_item):
    # 如果url相同，且属于云服务器域名的，返回true
    test_flag = False
    if list1_item[0] == list2_item[0] and list1_item[0] != [] and list1_item[0] != '' \
            and list1_item[0] and list1_item[0] != '[]' and list1_item[2] not in list_last_section:
        if list1_item[4]:# alpha domain
            if list1_item[4] not in list_no_use_domain:
                if test_flag:
                    pass
                else:
                    return True
        else:# digital domain
            str_tmp = str(list1_item[3][0])+'.'+str(list1_item[3][1])+'.'+str(list1_item[3][2])+'.'+str(list1_item[3][3])
            # print(str_tmp)
            if list1_item[3] and list2_item[3]:
                if test_flag:
                    pass
                else:
                    return True

    # flag_rn = False
    # if list1_item[11] and list2_item[11] and list1_item[11] != '[]' and list2_item[11] != '[]':
    #     if type(list1_item[11]) == str:
    #         list1_item[11] = eval(list1_item[11])
    #     if type(list2_item[11]) == str:
    #         list2_item[11] = eval(list2_item[11])
    #     flag_tmp = True
    #     for m in range(len(list1_item[11])):
    #         for n in range(len(list2_item[11])):
    #             if flag_tmp:
    #                 if list1_item[11][m] == list2_item[11][n]:
    #                     flag_rn = True
    #                     flag_tmp = False

    # 如果url结构类似，返回true
    if list1_item[4]:# alpha domain
        if list1_item[4] == list2_item[4] and list1_item[4] not in list_no_use_domain and \
            list1_item[5] == list2_item[5] and list1_item[6] == list2_item[6]\
            and list1_item[7] == list2_item[7] and list1_item[8] == list2_item[8] \
                and list1_item[9] == list2_item[9] and list1_item[10] == list2_item[10]and list1_item[8] > 4 :
            if test_flag:
                pass
            else:
                return True
    else:# digital domain
        if list1_item[3] and list2_item[3]:
            str_tmp = str(list1_item[3][0])+'.'+str(list1_item[3][1])+'.'+str(list1_item[3][2])+'.'+str(list1_item[3][3])
            str_tmp1 = str(list2_item[3][0])+'.'+str(list2_item[3][1])+'.'+str(list2_item[3][2])+'.'+str(list2_item[3][3])
            # print(str_tmp)
            if list1_item[3][0] == list2_item[3][0] and list1_item[3][1] == list2_item[3][1] and list1_item[3][2] == list2_item[3][2]\
                    and (str_tmp not in list_no_use_domain_all or str_tmp1 not in list_no_use_domain_all):
                if test_flag:
                    pass
                else:
                    return True

    # 如果url最后一部分相同，且结构类似，域名不属于云服务器，返回true
    if list1_item[4]:# alpha domain
        if list1_item[4] == list2_item[4] and list1_item[4] not in list_no_use_domain and list1_item[5] == list2_item[5] and list1_item[6] == list2_item[6] \
                and list1_item[7] == list2_item[7] and list1_item[8] == list2_item[8] \
                and list1_item[9] == list2_item[9] and list1_item[10] == list2_item[10] and list1_item[2] == list2_item[2] \
                and (list1_item[2] and list1_item[2] not in list_last_section) and list1_item[8] > 4 and list2_item[8] > 4 \
                or(list1_item[8] < 5 and list1_item[2] == list2_item[2] and list1_item[2] not in list_last_section
                   and list1_item[4] == list2_item[4] and list1_item[4] not in list_no_use_domain):
            if test_flag:
                pass
            else:
                return True
    else:# digital domain
        if list1_item[3] and list2_item[3]:
            str_tmp = str(list1_item[3][0]) + '.' + str(list1_item[3][1]) + '.' + str(list1_item[3][2]) + '.' + str(
                list1_item[3][3])
            # print(str_tmp)
            if list1_item[3][0] == list2_item[3][0] and list1_item[3][1] == list2_item[3][1] and list1_item[3][2] == list2_item[3][2] \
                    and list1_item[2] == list2_item[2] and list1_item[2] not in list_last_section:
                # print(str_tmp)
                if test_flag:
                    pass
                else:
                    return True

        # 测试 ip相同 返回true
        # if list1_item[4] and list2_item[4]:
        #     domain_tmp = list1_item[4] + '.' + list1_item[5]
        #     key_tmp_ = (sha11, domain_tmp)
        #     domain_tmp1 = list2_item[4] + '.' + list2_item[5]
        #     key_tmp_1 = (sha12, domain_tmp1)
        #     if key_tmp_ in dict_domain_ip.keys() and key_tmp_1 in dict_domain_ip.keys() \
        #             and domain_tmp not in list_no_use_domain_all and domain_tmp1 not in list_no_use_domain_all:
        #         ip1_list = dict_domain_ip[key_tmp_]
        #         ip2_list = dict_domain_ip[key_tmp_1]
        #
        #         for x in range(len(ip1_list)):
        #             for y in range(len(ip2_list)):
        #                 ip1 = ip1_list[x]
        #                 ip2 = ip2_list[y]
        #                 ip1_vec = str.split(ip1, ".")
        #                 ip2_vec = str.split(ip2, ".")
        #                 if ip1_vec[0] == ip2_vec[0] and ip1_vec[1] == ip2_vec[1] and ip1_vec[2] == ip2_vec[2]:
        #                     # print(domain_tmp,domain_tmp1)
        #                     return True

    # 如果中文关键字相同，且结构类似，返回true
    if list1_item[4]:
        if list1_item[1] == list2_item[1] and list1_item[1] in list_key_all and list1_item[4] == list2_item[4] and list1_item[5] == list2_item[5] and list1_item[6] == list2_item[6] \
                    and list1_item[7] == list2_item[7] and list1_item[8] == list2_item[8] \
                    and list1_item[9] == list2_item[9] and list1_item[10] == list2_item[10] and list1_item[4] not in list_no_use_domain:
            if test_flag:
                pass
            else:
                return True
    # 如果特殊中文关键字相同，则返回true
    if list1_item[1] == list2_item[1] and list1_item[1] in list_key:
        if test_flag:
            pass
        else:
            return True
    # if structure similar
    # if list1_item[4]:# alpha domain
    #     if list1_item[0] != list2_item[0] and list1_item[5] == list2_item[5] and list1_item[6] == list2_item[6] \
    #             and list1_item[7] == list2_item[7] and list1_item[8] == list2_item[8] \
    #             and list1_item[9] == list2_item[9] and list1_item[10] == list2_item[10] \
    #             and list1_item[2] == list2_item[2] and flag_rn and (list1_item[2] in list_sum_select and list2_item[2] in list_sum_select):
    #         # pass
    #         # print(list1_item,list2_item)
    #         return True

# 通过feature（）比较不同恶意样本的是否相同
def compare_url(list1, list2):
    if len(list1) == 0 or len(list2) == 0 or type(list1) == float \
            or list1 == "NaN" or type(list2) == float or list2 == "NaN":
        return False
    else:
        list1 = eval(list1)
        list2 = eval(list2)
    for i in range(len(list1)):
        for j in range(len(list2)):
            count_none = 0
            # delete all urls like /Domain/fty.me
            for m in range(len(list1[i])):
                if not list1[i][m]:
                    count_none += 1
            if count_none > 5:
                return False
            #
            # if not len(list1[i]):
            #     return False
            # print(list1[i])
            if feature(list1[i],list2[j]):
            #     print(list1[i][0])
                return True
    return False

for i in range(len(phone_number)):
    data_list.append([phone_number[i], email[i], url[i],domain[i],sha1[i]])

key_list = []
result_list = []

# 将过程数据保存在txt中
# file=open('idx/keyx.txt','r',encoding="utf-8")
# key_list = eval(file.readline())
# file.close()
#
# file=open('idx/resx.txt','r',encoding="utf-8")
# result_list = eval(file.readline())
# file.close()
#
# file=open('idx/idx.txt','r',encoding="utf-8")
# current_num = eval(file.readline())
# file.close()

# 实现聚类代码
for i in range(len(sha1)):
    flag_list = []
    if i % 1000 == 0:
        print("current step:", i)
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(nowTime)
        print("Key_List:", len(key_list))

    for j in range(len(key_list)):
        j_flag = True
        # 如果哈希phone相同，返回true
        if data_list[i][0] != "[]" and data_list[i][0] != "NaN":
            for k in range(len(key_list[j][0])):
                if data_list[i][0] == key_list[j][0][k] and data_list[i][0] != 'NaN':
                    if j not in flag_list:
                        # print(data_list[i][0])
                        flag_list.append(j)
                        j_flag = False
                    if not j_flag:
                        break
            if not j_flag:
                continue
        # 如果哈希email相同，返回true
        if data_list[i][1] != "[]" and data_list[i][1] != "NaN":
            for k in range(len(key_list[j][1])):
                if data_list[i][1] == key_list[j][1][k] and data_list[i][1] != 'NaN':
                    if j not in flag_list:
                        # print(data_list[i][1])
                        flag_list.append(j)
                        j_flag = False
                    if not j_flag:
                        break
            if not j_flag:
                continue

        # 如果url满足条件，返回true
        flag_show = True
        if data_list[i][2] != "[]" and data_list[i][2] != "NaN":
            for k in range(len(key_list[j][2])):
                if compare_url(data_list[i][2],key_list[j][2][k]):
                    flag = j
                    if j not in flag_list:
                        flag_list.append(j)
                        j_flag = False
                    if compare_url(data_list[i][2],key_list[j][2][k]) and flag_show:
                        print("url flag=", j)
                        print(key_list[j][2][k])
                        print(data_list[i][2])
                        flag_show = False
                    break

    # 如果flag-list空，则将数据加入keylist和resultlist列表；否则，则合并列表
    if not len(flag_list):
        # print(url_key_idx(data_list[i][7]))
        if (data_list[i][0] != "NaN" or data_list[i][1] != "NaN" or data_list[i][2] != "NaN" or data_list[i][3] != "NaN" ) and \
                (data_list[i][0] != "[]" or data_list[i][1] != "[]" or data_list[i][2] != "[]"or data_list[i][3] != "[]"):
            key_list.append([[data_list[i][0]], [data_list[i][1]], [data_list[i][2]], [data_list[i][3]]])
            result_list.append([data_list[i][-1]])
    else:
        first_idx = flag_list[0]
        # print(flag_list)
        # add key and res in the first index of key list
        if data_list[i][0] not in key_list[first_idx][0] and data_list[i][0] != "NaN" and data_list[i][0] != "[]":
            key_list[first_idx][0].append(data_list[i][0])
        if data_list[i][1] not in key_list[first_idx][1] and data_list[i][1] != "NaN" and data_list[i][1] != "[]":
            key_list[first_idx][1].append(data_list[i][1])
        if data_list[i][2] not in key_list[first_idx][2] and data_list[i][2] != "NaN" and data_list[i][2] != "[]":
            key_list[first_idx][2].append(data_list[i][2])
        if data_list[i][3] not in key_list[first_idx][3] and data_list[i][3] != "NaN" and data_list[i][3] != "[]":
            key_list[first_idx][3].append(data_list[i][3])
        result_list[first_idx].append(data_list[i][-1])

        # if flag_list's length > 1, the cluster is needed.
        flag_list.sort(reverse=True)
        # print(flag_list)
        for x in range(len(flag_list)-1):
            # print("delete target key:",key_list[flag_list[x]])
            # print("delete target res:",result_list[flag_list[x]])
            key_tmp = copy.deepcopy(key_list[flag_list[x]])
            res_tmp = copy.deepcopy(result_list[flag_list[x]])

            for m in range(len(key_tmp[0])):
                if key_tmp[0][m] not in key_list[first_idx][0]:
                    key_list[first_idx][0].append(key_tmp[0][m])
            for m in range(len(key_tmp[1])):
                if key_tmp[1][m] not in key_list[first_idx][1]:
                    key_list[first_idx][1].append(key_tmp[1][m])
            for m in range(len(key_tmp[2])):
                if key_tmp[2][m] not in key_list[first_idx][2]:
                    key_list[first_idx][2].append(key_tmp[2][m])
            for m in range(len(key_tmp[3])):
                if key_tmp[3][m] not in key_list[first_idx][3]:
                    key_list[first_idx][3].append(key_tmp[3][m])
            for m in range(len(res_tmp)):
                result_list[first_idx].append(res_tmp[m])

            del key_list[flag_list[x]]
            del result_list[flag_list[x]]

print(len(result_list))

# 保存数据
file=open('key3.txt','w',encoding="utf-8")
file.write(str(key_list))
file.close()

file=open('res3.txt','w',encoding="utf-8")
file.write(str(result_list))
file.close()


sha1_res = dict()
for i in range(len(sha1)):
    sha1_res[sha1[i]] = 0

for i in range(len(result_list)):
    for j in range(len(result_list[i])):
        sha1_res[result_list[i][j]] = i+1

count = len(result_list)

for i in range(len(sha1)):
    if not sha1_res[sha1[i]]:
        count += 1
        sha1_res[sha1[i]] = count

# file=open('key1.txt','w',encoding="utf-8")
# file.write(str(key_list))
# file.close()
#
# file=open('res1.txt','w',encoding="utf-8")
# file.write(str(result_list))
# file.close()

sha1_key = []
sha1_value = []


for i in sha1_res.keys():
    sha1_key.append(i)
    sha1_value.append(sha1_res[i])

dataframe = pd.DataFrame({"id":sha1_value,
                          "sha1":sha1_key})
dataframe.to_csv("trace2/results/trace2-step3.csv",index=False,sep=",",encoding='utf_8_sig')

