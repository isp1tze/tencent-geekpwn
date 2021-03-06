import pandas as pd
import re
from utils import *

target = pd.read_csv('trace2/results/trace2-step4.csv',encoding='utf_8_sig')

target = target.fillna('NaN')

phone = target.get('phone')
email = target.get('email')
sha1 = target.get('sha1')
domain = target.get('domain')
url = target.get('url')


target0 = pd.read_csv('./phase2/trace2_test/fqdn_reginfo.csv',encoding='utf_8_sig')

target0 = target0.fillna('NaN')


#
sha10 = target0.get('sha1')
email0 = target0.get('email_address')
domain0 = target0.get('domain')

dict_domain_email = dict()

for i in range(len(sha10)):
    if email0[i] != 'NaN':
        if (sha10[i],domain0[i]) not in dict_domain_email.keys():
            dict_domain_email[(sha10[i],domain0[i])] = [email0[i]]
        else:
            dict_domain_email[(sha10[i], domain0[i])].append(email0[i])
    # else:
    #     print('nan')

print(dict_domain_email.values())

# target2 = pd.read_csv('./phase2/trace2_test/fqdn_ip.csv',encoding='utf_8_sig')
#
# target2 = target2.fillna('NaN')
#
#
# #
# sha12 = target2.get('sha1')
# ip2 = target2.get('ip')
# site2 = target2.get('site')
#
#
# def process_domain_std(domain_str1):
#     domain_str = domain_str1.split('.')
#     # print(len(domain_str))
#     if len(domain_str) > 2:
#         if domain_str[-2] != 'com':
#             return domain_str[-2]+'.'+domain_str[-1]
#         else:
#             return domain_str[-3] + '.' + domain_str[-2] + '.' + domain_str[-1]
#     else:
#         return domain_str1
#
# for i in range(len(site2)):
#     site2[i] = process_domain_std(site2[i])
#
# dict_domain_ip = dict()
#
# for i in range(len(sha12)):
#     if site2[i] != 'NaN':
#         if (sha12[i],site2[i]) not in dict_domain_ip.keys():
#             dict_domain_ip[(sha12[i],site2[i])] = [ip2[i]]
#         else:
#             dict_domain_ip[(sha12[i], site2[i])].append(ip2[i])
#     else:
#         print('nan')

import datetime,copy

key_list , result_list, data_list = [], [], []


for i in range(len(phone)):
    # if phone_number[i] and email[i] and sha1[i]:
    data_list.append([phone[i], email[i], url[i],domain[i],sha1[i]])

# 通过feature（）比较不同恶意样本的是否相同
def compare_url(list1, list2, sha11, sha12):
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

            # print(sha11,sha12)
            #
            # if not len(list1[i]):
            #     return False

            if feature1(list1[i],list2[j], sha11,sha12):
            #     print(list1[i][0])
                return True
            # if feature2(list1[i],list2[j]):
            #     return True
    return False

# f = open('process-data/domain.txt', encoding='utf-8')
# r = f.readline()
# list_domain = []
# while(r):
#     tmp = r.split("'")
#     if len(tmp) > 1:
#         tmp1 = tmp[1].split('.')[0]
#         list_domain.append(tmp1)
#     # tmp = r.replace("\n","")
#     # list_key.append(tmp)
#     r = f.readline()
import math

# 测试分类特征
def feature1(list1_item, list2_item, sha11,sha12):
    # if url same then return true
    # flag_digital = False
    # flag_alpha = False
    # # print(list1_item)
    #
    # # return True
    # flag_rn = False
    # if list1_item[11] and list2_item[11] and list1_item[11] != '[]' and list2_item[11] != '[]':
    #     # print(type(list1_item[11]), type(list2_item[11]))
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
    #
    # if list1_item[7]:
    #     if list1_item[4] == list2_item[4] and list1_item[2] == list2_item[2] and list1_item[5] == list2_item[5] and list1_item[6] == list2_item[6] \
    #             and list1_item[7] == list2_item[7] and list1_item[8] == list2_item[8] \
    #             and list1_item[9] == list2_item[9] and list1_item[10] == list2_item[10] \
    #             and list1_item[4] in list_domain and list1_item[2] in list_sum_select:
    #         return True
    #
    # if list1_item[1] == list2_item[1] and list1_item[1] in list_key and list1_item[5] == list2_item[5] and list1_item[6] == list2_item[6] \
    #             and list1_item[7] == list2_item[7] and list1_item[8] == list2_item[8] \
    #             and list1_item[9] == list2_item[9] and list1_item[10] == list2_item[10]:
    #     pass
    #     # return True
    #
    # return flag_digital or flag_alpha

    # if list1_item[0] == list2_item[0] and list1_item[0] != [] and list1_item[0] != '' \
    #         and list1_item[0] and list1_item[0] != '[]' and list1_item[2] in list_sum_select:
    #     if list1_item[4]:# alpha domain
    #         if list1_item[4] in list_domain_use:
    #             pass
    #             # return True
    #     else:# digital domain
    #         str_tmp = str(list1_item[3][0])+'.'+str(list1_item[3][1])+'.'+str(list1_item[3][2])+'.'+str(list1_item[3][3])
    #         # print(str_tmp)
    #         if list1_item[3] and list2_item[3]:
    #             print(str_tmp)
    #             # pass
    #             return True
    #
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
    # if domain similar

    # if list1_item[4]:# alpha domain
    #     if list1_item[4] == list2_item[4] and list1_item[4] not in list_no_use_domain and \
    #         list1_item[5] == list2_item[5] and list1_item[6] == list2_item[6]\
    #         and list1_item[7] == list2_item[7]and list1_item[8] == list2_item[8] \
    #         and list1_item[9] == list2_item[9]and list1_item[10] == list2_item[10]:
    #         #     and
    #         # pass
    #         return True
    # else:# digital domain
    #     if list1_item[3] and list2_item[3]:
    #         str_tmp = str(list1_item[3][0])+'.'+str(list1_item[3][1])+'.'+str(list1_item[3][2])+'.'+str(list1_item[3][3])
    #         str_tmp1 = str(list2_item[3][0])+'.'+str(list2_item[3][1])+'.'+str(list2_item[3][2])+'.'+str(list2_item[3][3])
    #         # print(str_tmp)
    #         if list1_item[3][0] == list2_item[3][0] and list1_item[3][1] == list2_item[3][1] and list1_item[8] == list2_item[8] \
    #         and list1_item[9] == list2_item[9]and list1_item[10] == list2_item[10] \
    #                 and (str_tmp in list_domain_use_all or str_tmp1 in list_domain_use_all):
    #             # print(str_tmp)
    #             pass
    #             # return True


    # print(sha11,sha12)


    # ip same
    # if list1_item[4] and list2_item[4]:
    #     domain_tmp = list1_item[4]+'.'+list1_item[5]
    #     key_tmp_ = (sha11,domain_tmp)
    #     domain_tmp1 = list2_item[4]+'.'+list2_item[5]
    #     key_tmp_1 = (sha12,domain_tmp1)
    #     if key_tmp_ in dict_domain_ip.keys() and key_tmp_1 in dict_domain_ip.keys() \
    #             and domain_tmp not in list_no_use_domain_all and domain_tmp1 not in list_no_use_domain_all:
    #         ip1_list = dict_domain_ip[key_tmp_]
    #         ip2_list = dict_domain_ip[key_tmp_1]
    #
    #         for x in range(len(ip1_list)):
    #             for y in range(len(ip2_list)):
    #                 ip1 = ip1_list[x]
    #                 ip2 = ip2_list[y]
    #                 ip1_vec = str.split(ip1,".")
    #                 ip2_vec = str.split(ip2,".")
    #                 if ip1_vec[0] == ip2_vec[0] and ip1_vec[1] == ip2_vec[1] and ip1_vec[2] == ip2_vec[2]:
    #                     # print(domain_tmp,domain_tmp1)
    #                     return True

    # if list1_item[4] and list2_item[4]:
    #     domain_tmp = list1_item[4]+'.'+list1_item[5]
    #     key_tmp_ = (sha11,domain_tmp)
    #     domain_tmp1 = list2_item[4]+'.'+list2_item[5]
    #     key_tmp_1 = (sha12,domain_tmp1)
    #     if key_tmp_ in dict_domain_email.keys() and key_tmp_1 in dict_domain_email.keys() \
    #             and domain_tmp not in list_no_use_domain_all and domain_tmp1 not in list_no_use_domain_all:
    #         ip1_list = dict_domain_email[key_tmp_]
    #         ip2_list = dict_domain_email[key_tmp_1]
    #
    #         for x in range(len(ip1_list)):
    #             for y in range(len(ip2_list)):
    #                 ip1 = ip1_list[x]
    #                 ip2 = ip2_list[y]
    #                 if ip1 == ip2 and ip1 not in list_emailnouse:
    #                     # print(domain_tmp,domain_tmp1)
    #                     return True

    # list1_item[5] == list2_item[5] and list1_item[6] == list2_item[6] \
    # and list1_item[7] == list2_item[7] and list1_item[8] == list2_item[8] \
    # and list1_item[9] == list2_item[9] and list1_item[10] == list2_item[10] \
    # and


    # if last_sentence similar
    # if list1_item[4]:# alpha domain
    #     if (list1_item[4] == list2_item[4] and list1_item[4] not in list_no_use_domain
    #            and list1_item[2] == list2_item[2] and list1_item[2] not in list_last_section and list2_item[2] not in list_last_section):
    #         #and list1_item[2] and list2_item[2] and list1_item[2] == list2_item[2]
    #         return True
    #
    # if list1_item[4]:# alpha domain
    #     if (list1_item[4] == list2_item[4] and list1_item[4] not in list_no_use_domain
    #            and list1_item[1] == list2_item[1] and list1_item[1] in list_key_all):
    #         #and list1_item[2] and list2_item[2] and list1_item[2] == list2_item[2]
    #         return True

    # key
    if list1_item[1] == list2_item[1] and list1_item[1] in list_key:
        return True


    # else:# digital domain
    #     if list1_item[3] and list2_item[3]:
    #         str_tmp = str(list1_item[3][0]) + '.' + str(list1_item[3][1]) + '.' + str(list1_item[3][2]) + '.' + str(
    #             list1_item[3][3])
    #         str_tmp1 = str(list2_item[3][0]) + '.' + str(list2_item[3][1]) + '.' + str(list2_item[3][2]) + '.' + str(
    #             list2_item[3][3])
    #         # print(str_tmp)
    #         if list1_item[3][0] == list2_item[3][0] and list1_item[3][1] == list2_item[3][1] and list1_item[3][2] == list2_item[3][2] \
    #                 and  list1_item[8] == \
    #                 list2_item[8] and list1_item[9] == list2_item[9] and list1_item[10] == list2_item[10] \
    #                 and list2_item[2] not in list_last_section and list1_item[2] not in list_last_section \
    #                 and (str_tmp not in list_no_use_domain_all or str_tmp1 not in list_no_use_domain_all):
    #             # print(str_tmp)
    #             # pass
    #             return True
    #
    # key
    # if list1_item[1] == list2_item[1] and list1_item[1] in list_key:
    #     return True


    # if list1_item[4]:
    #     if list1_item[1] == list2_item[1] and list1_item[1] in list_key_all and list1_item[4] == list2_item[4] and list1_item[5] == list2_item[5] and list1_item[6] == list2_item[6] \
    #                 and list1_item[7] == list2_item[7] and list1_item[8] == list2_item[8] \
    #                 and list1_item[9] == list2_item[9] and list1_item[10] == list2_item[10] and list1_item[4] not in list_no_use_domain:
    #         return True
    #
    # list_english_key = ['/cache/cdchanghongktwx.com/',
    #                     'UploadFiles/admin/']
    #
    # # '/bigfiles/apk/516141/201605/09c18fd3702bb84ac3593a1808f86add1463469741',
    # # '/c3pr90ntc0td/',
    # if list1_item[0] and list2_item[0]:
    #     for i in range(len(list_english_key)):
    #         if list_english_key[i] in list1_item[0] and list_english_key[i] in list2_item[0]:
    #             return True


    # pass

    # if list1_item[4]:# alpha domain
    #     if list1_item[4] in list_domain_use and list1_item[4] == list2_item[4]:
    #         # pass
    #         return True

# 测试分类特征
def feature2(list1_item, list2_item):

    flag_digital = False

    flag_alpha = False



        # else:
        #     flag_alpha = (list1_item[4] == list2_item[4] and list1_item[7] > 3\
        #              and list1_item[4] not in list_domain and list1_item[4] and list2_item[4])

    # print(flag_digital or flag_alpha)

    flag = list1_item[2] == list2_item[2] and list1_item[2]  \
           and (flag_digital or flag_alpha)\
           and 1 > math.fabs(int(list1_item[8]) - int(list2_item[8])) \
           and 1 > math.fabs(int(list1_item[10]) - int(list2_item[10]))and list1_item[9] == list2_item[9]

    return flag

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

        # if  data_list[i][3] != "[]" and data_list[i][3] != "NaN": # (data_list[i][2] == "[]" or data_list[i][2] == "NaN") and
        #     if data_list[i][3]:
        #         for k in range(len(key_list[j][3])):
        #             if key_list[j][3][k] and key_list[j][3][k] != 'NaN':
        #                 data_tmp = eval(data_list[i][3])
        #                 key_tmp = eval(key_list[j][3][k])
        #                 # print(data_tmp,key_tmp)
        #                 for x in range(len(data_tmp)):
        #                     for y in range(len(key_tmp)):
        #                         if data_tmp[x] == key_tmp[y]:
        #                             # print(data_tmp[x],key_tmp[y])
        #                             # pass
        #                             if data_tmp[x] not in list_no_use_domain_all:
        #                                 if j not in flag_list:
        #                                     flag_list.append(j)
        #                                 j_flag = False
        #                                 print(data_tmp[x])
        #                         if not j_flag:
        #                             continue
        # flag_show = True
        # if data_list[i][2] != "[]" and data_list[i][2] != "NaN":
        #     for k in range(len(key_list[j][2])):
        #         if compare_url(data_list[i][2],key_list[j][2][k], data_list[i][-1],result_list[j][k]):
        #             flag = j
        #             if j not in flag_list:
        #                 flag_list.append(j)
        #             if compare_url(data_list[i][2],key_list[j][2][k],data_list[i][-1],result_list[j][k]) and flag_show:
        #                 print("url flag=", j)
        #                 print(key_list[j][2][k])
        #                 print(data_list[i][2])
        #                 flag_show = False

    # 如果flag-list空，则将数据加入keylist和resultlist列表；否则，则合并列表
    if not len(flag_list):
        # print(url_key_idx(data_list[i][7]))
        if (data_list[i][0] != "NaN" or data_list[i][1] != "NaN" or data_list[i][2] != "NaN" or data_list[i][3] != "NaN" ) and \
                (data_list[i][0] != "[]" or data_list[i][1] != "[]" or data_list[i][2] != "[]"or data_list[i][3] != "[]"):
            key_list.append([[data_list[i][0]], [data_list[i][1]], [data_list[i][2]], [data_list[i][3]]])
            result_list.append([data_list[i][-1]])
    else:
        first_idx = flag_list[0]
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


sha1_res = dict()
for i in range(len(sha1)):
    sha1_res[sha1[i]] = 0

# 设置该异常庞大数据的类别从20000开始计数
for i in range(len(result_list)):
    for j in range(len(result_list[i])):
        sha1_res[result_list[i][j]] = 20000 + i+1

count = len(result_list)

for i in range(len(sha1)):
    if not sha1_res[sha1[i]]:
        # count += 1
        sha1_res[sha1[i]] = 20000 + count



sha1_key = []
sha1_value = []

# for i in range(500):
#     print(key_list[i])

for i in sha1_res.keys():
    sha1_key.append(i)
    sha1_value.append(sha1_res[i])

dataframe = pd.DataFrame({"id":sha1_value,
                          "sha1": sha1_key})

# 数据存储
target1 = pd.read_csv('trace2/results/trace2-step3.csv',encoding='utf_8_sig')

target1 = target1.fillna('NaN')
sha11 = target1.get('sha1')
id1 = target1.get('id')
dict1 = dict()


# 数据转换
dataframe.to_csv("trace2/results/trace2-step5.csv",index=False,sep=",",encoding='utf_8_sig')
target = pd.read_csv('trace2/results/trace2-step3.csv',encoding='utf_8_sig')
target = target.fillna('NaN')

sha1 = target.get('sha1')
id = target.get('id')
sha1_res = dict()

target1 = pd.read_csv('trace2/results/trace2-step5.csv',encoding='utf_8_sig')
target1 = target1.fillna('NaN')
sha11 = target1.get('sha1')
id1 = target1.get('id')

for i in range(len(sha11)):
    sha1_res[sha11[i]] = id1[i]


for i in range(len(id)):
    if id[i] == 33:
        if sha1[i] in sha1_res.keys():
            print(i, sha1_res[sha1[i]])
            id[i] = sha1_res[sha1[i]]
        else:
            print("Error:",sha1[i])


dataframe = pd.DataFrame({"id":id,
                          "sha1": sha1})

dataframe.to_csv("trace2/results/trace2-step5-final.csv",index=False,sep=",",encoding='utf_8_sig')
