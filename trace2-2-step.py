import pandas as pd
import re
from urllib import parse

from utils import *

list_new_key = []

# 删除重复和nan数据
def delete_nan_and_repeat(input_list):
    for i in range(len(input_list)):
        if type(input_list[i]) != float:
            # print(register_username[i])
            # print(input_list[i])
            input_list[i] = eval(input_list[i])
            new_input = []
            for id in input_list[i]:
                if id not in new_input and id != 'nan':
                    new_input.append(id)
            input_list[i] = new_input
            for j in range(len(input_list[i])):
                input_list[i] = str(input_list[i])
            # print(input_list[i])
    return input_list

# 提取中文关键字
def extract_key(str_input):
    str_input = str_input.replace('/', '').replace('.', '') \
        .replace(':', '').replace('_', '').replace('-', '') \
        .replace('&', '').replace('=', '').replace('?', '')
    return re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", str_input)

# 提取中文关键字
def extract_apk(str_url):
    str_tmp = str_url.split("/")
    str_tmp1 = str_tmp[-1].split(".")
    if len(str_tmp1) > 1:
        # if str_tmp[-2] in list_apk:
        return str_tmp[-1]
    else:
        # if str_tmp[-1] in list_fuc:
        return str_tmp[-1]

# 处理domain
def process_domain(domain_str1):
    domain_str = domain_str1.split('.')
    for i in range(3):
        if not domain_str[i].isdigit():
            return False
    return True

# 处理domain为IP类数据
def process_digital(str_input1):
    str_input = str_input1.split(".")
    return [str_input, None, None, None, None]

# 处理domain是否为非IP类数据
def process_alpha(str_input1):
    str_input = str_input1.split(".")
    if len(str_input)<2:
        return [None, None, None, None, None]
    else:
        if str_input[-2] != 'com':
            tmp_domain = process_sub_section(str_input[-2])
            return [None, str_input[-2],str_input[-1], tmp_domain[0], tmp_domain[1]]
        else:
            tmp_domain = process_sub_section(str_input[-3])
            return [None, str_input[-3], str_input[-2] + '.'+str_input[-1], tmp_domain[0], tmp_domain[1]]

# 处理url中domain后一部分/xxxxx/特征
def process_sub_section(str_input1):
    count = len(str_input1) if str_input1 else None
    if str_input1.isdigit():
        return [0,count]
    if str_input1.isalpha():
        return [1,count]
    if str_input1.isalnum():
        return [2,count]

    return [None,count]

# 处理url特征
def process_url_class(str_url):
    # 去除www.
    str_url = str_url.replace("www.","")
    str_tmp = str_url.split("/")
    if len(str_tmp) >= 4:
        # 处理带/数目超过3的url
        sub_sec = process_sub_section(str_tmp[3])
        if process_domain(str_tmp[2]):
            tmp = process_digital(str_tmp[2])
            tmp.append(len(str_tmp))
            tmp.append(sub_sec[0])
            tmp.append(sub_sec[1])
            return tmp
        else:
            tmp = process_alpha(str_tmp[2])
            tmp.append(len(str_tmp))
            tmp.append(sub_sec[0])
            tmp.append(sub_sec[1])
            return tmp
    else:
        return [None, None, None, None, None, None, None, None]

# 处理带/数据
def process_unquote(str_url1):
    tmp_list = str_url1.split("/")
    res = ""
    for i in range(len(tmp_list)):
        if i != 0:
            res += "/" + parse.unquote(tmp_list[i])
        else:
            res += parse.unquote(tmp_list[i])
    return res

id_dict = dict()

# 处理url
def process_url(input_list,register_username,email_address,site,domain,ip):
    for i in range(len(input_list)):
        if type(input_list[i]) != float:
            # print(register_username[i])
            # print(input_list[i])
            if input_list[i]:
                input_list[i] = eval(input_list[i])
            new_input_list = []
            count_one_url_list = 0
            MAX_ONE_URL_NUM = 20
            for id_original in input_list[i]:
                count_one_url_list += 1
                # limit the length of current
                if count_one_url_list > MAX_ONE_URL_NUM:
                    break
                id_original = process_unquote(id_original)
                print(id_original)
                new_input = [id_original]
                id = extract_key(id_original)
                if id not in id_dict.keys():
                    id_dict[id] = 1
                else:
                    id_dict[id] += 1

                # print(id)
                # url key last_apk

                # if id in list_key:
                if id != 'nan' and id !='' and id:
                    new_input.append(id)
                    if id not in list_new_key:
                        list_new_key.append(id)
                else:
                    new_input.append(None)
                id = extract_apk(id_original)
                # print(id)
                if id != 'nan' and id != '' and id:
                    new_input.append(id)
                    if id not in list_new_key:
                        list_new_key.append(id)
                else:
                    new_input.append(None)
                tmp_list = process_url_class(id_original)
                for m in range(len(tmp_list)):
                    new_input.append(tmp_list[m])

                if str(register_username[i]) == 'nan':
                    new_input.append(None)
                else:
                    new_input.append(str(register_username[i]))
                #
                if str(domain[i]) == 'nan':
                    new_input.append(None)
                else:
                    new_input.append(str(domain[i]))


                new_input_list.append(new_input)
                # print(len(new_input))

            input_list[i] = new_input_list
            for j in range(len(input_list[i])):
                input_list[i] = str(input_list[i])
                # print(input_list[i])
    return input_list

target = pd.read_csv('trace2/results/trace2-step1.csv',encoding='utf_8_sig')

phone_number = target.get('phone_number')#phone_number')

contain_email = target.get('contain_email')

sha1 = target.get('sha1')

site = target.get('site')

domain = target.get('domain')

ip = target.get('ip')

register_username = target.get('register_username')

email_address = target.get('email_address')

url = target.get('url')


url = delete_nan_and_repeat(url)

register_username = delete_nan_and_repeat(register_username)
email_address = delete_nan_and_repeat(email_address)
site = delete_nan_and_repeat(site)
domain = delete_nan_and_repeat(domain)
ip = delete_nan_and_repeat(ip)

import copy

url1 = copy.deepcopy(url)
url1 = process_url(url1,register_username,email_address,site,domain,ip)



dataframe = pd.DataFrame({"phone_number":phone_number,
                        "contain_email":contain_email,
                        "sha1":sha1,
                        # "site":site,
                        "domain":domain,
                        # "register_username":register_username,
                        # "ip": ip,
                        # "url":url,
                        "url1": url1,
                        "email_address":email_address})

dataframe.to_csv("trace2/results/trace2-step2.csv",index=False,sep=",",encoding='utf_8_sig')

list1 = sorted(id_dict.items(), key=lambda d: d[1])

for i in range(len(list1)):
    print(list1[i])
