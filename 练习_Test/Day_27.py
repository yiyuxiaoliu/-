#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 
# @Desc    :

# aliens_0 = []
# for aliens_number in range(0, 30):
#     aliens_1 = {'color': 'green' ,'age': '18', 'name': 'liuzhen'}
#     aliens_0.append(aliens_1)
# for aliens_2 in aliens_0[:5]:
#     print(aliens_2)
# print(aliens_0)

# aliens_0 = {
#            'vlous':{
#                'age': 'llu',
#                'name': 'liuzhen',
#                'first': 'diyi'
#                },
#            'alien':{
#                'age': 'xiaoliu',
#                'last': 'zhenliu'
#                }
#       }
# for name , language in aliens_0.items():
#     print("这是一个i给名字:", name)
#     for i in language.items():
#         print(i)

#  用户输入和 while  循环：
# count = 0
# aliens_0 = int(input("这是一个测试需要："))
# while count <= 5:
#     if aliens_0 % 2 == 0:
#         print("这是偶数")
#         count = count + 1
#
#     else:
#         print("这是奇数")
#         break

aliens_0 = ""
while aliens_0 != 5:
    aliens_0 = input("请输入：")
    print(aliens_0)
    print(type(aliens_0))
