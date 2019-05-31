#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 
# @Desc    :

# def fun_lanuage( age, name, alien = ''):
#     """这是一个测试连续"""
#     if alien:
#         alien = age + name + alien
#     else:
#         alien = age + name
#     return alien.title()
#
# while True:
#     abs_1 = input("输入年龄：")
#     abs_2 = input("输入名字：")
#     abs_3 = input("输入性别：")
#     alien_0 = fun_lanuage(abs_1 , abs_2 ,abs_3)
#     print(alien_0)

#传递列表
#
# def Fun_lan(name):
#     for nam in name:
#         na = "Hello, " + nam.title() + "!"
#         print(na)
#
# username = ['liu', 'zhen', 'liuzhen']
# Fun_lan(username)

# def print_models(unprinted_designs, completed_models):
#     """
#     模拟打印每个设计，直到没有未打印的设计为止
#     打印每个设计后，都将其移到列表 completed_models 中
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         #  模拟根据设计制作 3D 打印模型的过程
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     """ 显示打印好的所有模型 """
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# def aliens_0(name, age):
#     while name:
#         aliens_1 = name.pop()
#         print("这是第一个不变的："+ aliens_1)
#         age.append(aliens_1)
# def ali(password):
#     for i in password:
#         print(i)
# aliens = ['name', 'age', 'asd']
# alien = []
# aliens_0(aliens, alien)
# ali(alien)

# def aliens_0(*name):
#     print(name)
# aliens_0('zhen', 'liu', 'liuzhen')

def build_profile(first, last, **user_info):
    """ 创建一个字典，其中包含我们知道的有关用户的一切 """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
        return profile
user_profile = build_profile('2', 'einstein',
                             hhh='princeton',
                             field='physics')
print(user_profile)