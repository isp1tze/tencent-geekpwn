# import pandas as pd
# # -*- coding: utf-8 -*-
# target = pd.read_csv('trace2-new.csv',encoding='utf_8_sig')
#
# register_username = target.get('register_username')
# email_address = target.get('email_address')
#
#
#
# def count_num(input_list):
#     dict_all = dict()
#     for i in range(len(input_list)):
#         if type(input_list[i]) != float:
#             # print(register_username[i])
#             # print(input_list[i])
#             input_list[i] = eval(input_list[i])
#             for id in input_list[i]:
#                 if id in dict_all.keys():
#                     dict_all[id] += 1
#                 else:
#                     dict_all[id] = 0
#             # print(input_list[i])
#     return dict_all
#
# dict_all = count_num(register_username)
#
# list1 = (sorted(dict_all.items(), key=lambda d: d[1]))
# # print(len(list1))
# for i in range(len(list1)):
#     print(list1[i][0])

from urllib import parse
print(parse.unquote("%E4%BD%93%E6%A3%80%E6%8A%A5%E5%91%8A%E5%8D%95"))



import re
str = "hello,world!!%[545]你好234世界。。。"
str = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", str)
str1 = "hello,world!!%[545]你好234世界。。。"
str1 = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", str1)
print(str==str1)

apk_dict = []
apk_dict_num = []

no_apk_dict = []
no_apk_dict_num = []

import pandas as pd

target = pd.read_csv('results/trace2.csv',encoding='utf_8_sig')
url = target.get('url')
all_dict = dict()

domain = target.get('register_username')

domain_dict = dict()

for i in range(len(domain)):
    if type(domain[i]) != float:
        domain_tmp = eval(domain[i])
        for j in range(len(domain_tmp)):
            if domain_tmp[j] not in domain_dict.keys():
                domain_dict[domain_tmp[j]] = 1
            else:
                domain_dict[domain_tmp[j]] += 1

# for k,v in domain_dict.items():
#     print(k,v)




def process_domain(domain_str):
    domain_str = domain_str.split('.')
    for i in range(3):
        if not domain_str[i].isdigit():
            return False
    return True

def process_digital(str_input):
    str_input = str_input.split(".")
    return [str_input[0]]

def process_alpha(str_input):
    str_input = str_input.split(".")
    if len(str_input)<2:
        return False
    else:
        return [str_input[-2],str_input[-1]]

def process_url(str_url):
    str_url = str_url.replace("www.","")
    str_tmp = str_url.split("/")
    if len(str_tmp) >= 4:
        # print(len(str_tmp), str_tmp[3],str_tmp[2])
        if process_domain(str_tmp[2]):
            print(process_digital(str_tmp[2]))
        else:
            print(process_alpha(str_tmp[2]))

def process_1st(str_url):
    str_tmp = str_url.split("/")
    str_tmp = str_tmp[-1].split(".")
    if len(str_tmp) > 1:
        if parse.unquote(str_tmp[-2])+"."+str_tmp[-1] not in apk_dict:
            apk_dict.append(parse.unquote(str_tmp[-2])+"."+str_tmp[-1])
            apk_dict_num.append(1)
        else:
            apk_dict_num[apk_dict.index(parse.unquote(str_tmp[-2])+"."+str_tmp[-1])] += 1
    else:
        if parse.unquote(str_tmp[-1]) not in no_apk_dict:
            no_apk_dict.append(parse.unquote(str_tmp[-1]))
            no_apk_dict_num.append(1)
        else:
            no_apk_dict_num[no_apk_dict.index(parse.unquote(str_tmp[-1]))] += 1




for i in range(len(url)):
    if type(url[i]) != float:
        str1 = eval(url[i])
        for j in range(len(str1)):
            str_tmp = str1[j]
            # process_url(str_tmp)
            process_1st(str_tmp)
            str1[j] = str1[j].replace('/', '').replace('.', '')\
                .replace(':', '').replace('_', '').replace('-','')\
                .replace('&','').replace('=','').replace('?','')
            tmp = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", str1[j])
            if tmp:
                if tmp not in all_dict.keys():
                    all_dict[tmp] = 1
                else:
                    all_dict[tmp] += 1

list1 = sorted(all_dict.items(), key=lambda d: d[1])
# print(len(list1))
apk_dict_dict = dict()
for i in range(len(apk_dict)):
    apk_dict_dict[apk_dict[i]] = apk_dict_num[i]


list1 = sorted(apk_dict_dict.items(), key=lambda d: d[1])


no_apk_dict_dict = dict()
for i in range(len(no_apk_dict)):
    no_apk_dict_dict[no_apk_dict[i]] = no_apk_dict_num[i]


list1 = sorted(domain_dict.items(), key=lambda d: d[1])

for i in range(len(list1)):
    print(list1[i])




# f2 = open('chinese1.txt','w')
# for i in range(len(list1)):
#     f2.write(list1[i])
#     f2.write("\n")
#
# f2.close()



