#!/usr/bin/env  python
# coding:utf-8
from __future__ import division

'''
计算给定字符的二进制信息熵（如有小数，保留至小数位后7位）                               
输入
输入任意一串字符
样例输入
aaaabbcd
输出
计算出字符串的信息熵
样例输出
1.75
'''
import math

def shangCount(adj):
    string = adj
    str_list = list(string)
    n = len(str_list)
    str_list_single = list(set(str_list))
    num_list = []
    for i in str_list_single:
        num_list.append(str_list.count(i))
    list_two = {}
    for i, j in zip(str_list_single, num_list):
        list_two.update({i: j})
    entropy = 0
    for j in str_list_single:
        entropy += -1 * (float(list_two[j] / n)) * math.log(float(list_two[j] / n), 2)
    if len(str(entropy).split('.')[-1]) >= 7:
        print('%.7f' % entropy)
    else:
        print(entropy)
