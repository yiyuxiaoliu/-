#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 
# @Desc    :

def heshui(*args):
    su = 0
    for i in args:
        su = su + i
    return su
summ = heshui(23,23,23,23,23,23,23)
print(summ)