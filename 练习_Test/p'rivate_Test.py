#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 
# @Desc    :

class Student():
    def __init__(self, name, alien):
        self.__name = name
        self.__alien = alien

    def print_alien(self):
        print(self.__name + self.__alien)

    def get_name(self):  # 外部代码要获取
        return self.__name
    def set_name(self, name):    # 允许外部代码修改
        self.__name = name

    def get_alien(self):    # 外部代码要获取
        return self.__alien
    def set_alien(self, alien):    # 允许外部代码修改
        self.__alien = alien


class Dog(Student):
    pass


dog = Dog('li', 'asd')
dog.print_alien()

