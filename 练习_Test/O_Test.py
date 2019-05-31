#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 
# @Desc    :
#
# with open('file.txt') as file_object:
#         il = file_object.readline()
# pi_string =''
# for i in il:
#      pi_string += i.rstrip()
# happy = input("请输入：")
# if happy in pi_string:
#     print("效果图")
# else:
#     print("不一样")

file_name = 'file.txt'
with open(file_name, 'a') as file:
    file.write('这是一个什么.\n')