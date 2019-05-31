#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 
# @Desc    :
peoper = ["张小青" ,"刘振" ,"振大大"]
for i in peoper:
    print("今天参加晚宴的人有：" ,i )
peo = peoper.pop(1)
pepe = peoper.insert(1,"小六个")
print("刚接到消息有一位嘉宾无法赴约：",peo,"因此需要另外邀请一位嘉宾:",peoper[1])
for i in peoper:
    print("截止目前参加人员有：",i)
print("刚刚收到一个更大的餐桌：再邀请三人")
peoper.insert(0,"张三")
peoper.insert(len(peoper)-2,"李四")
peoper.append("王二")
for i in peoper:
    print("今天参加晚宴的人有：" ,i )
print("刚刚得到消息，只能邀请二人：")
print(peoper)
a = sorted(peoper)

print(a)
print(peoper)
