#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 
# @Desc    : 单继承/多继承

class Get_first():
    # 定义基本属性；空字符，存储
    name = ''
    age = 0
    # 定义私用变量，私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法
    def __init__(self, n, a, w):
        self.nam = n
        self.age = a
        self.__weight = w
    def speak(self):
        print(self.nam , self.age, self.__weight)
# 单继承
class liu(Get_first):
    grade = ''
    def __init__(self, n, a, w, g):
        # 调用父类的构造函数
        Get_first.__init__(self, n, a, w)
        self.grade = g
        # 覆写父类的方法
    def speak(self):
        print(self.name , self.age, self.grade)
    @classmethod   # 类方法
    def b_print(cls):  # 当前类
        print(cls.__name__)  # 获取当前类
# # 实例化类子类
# s = liu('ken', 10, 60, 3)
# s.speak()
# 实例化父类
a = Get_first('liu', 10 , 20)  # 私用变量不能从其他类里面调用，
a.speak()
liu.b_print()  # 调用类方法

# 另一个类，多重继承之前的准备
class zhen():
    top = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.top = t
    def speak(self):
        print(self.name, self.top)
# 多重继承
class liuzhen(liu, zhen):
    a = ''
    def __init__(self, n, a, w, g, t):
        liu.__init__(self, n, a, w, g)
        zhen.__init__(self,n, t)

test = liuzhen('Eric', 25, 39, 39, 'PYTHON')
#  方法名相同，默认调用的是在括号中排前的父类的方法
test.speak()

# 3、方法重写，父类方法不能满足你的需求，可以子类重写父类
class Mothon():
    def MyMothod(self):
        print('调用父类方法')
class Chid(Mothon):
    # 定义子类
    def MyMothod(self):
        print('调用子类方法')
c = Chid()
c.MyMothod()

# python装饰器代替set get方法
# 第一种；变量的访问和设置，我们可以使用get、set方法
class student():
    def __init__(self, name):
        self.__name = name
    def get_name(self):   # 获得
        return self.__name
    def set_name(self, name):  # 设置
        self.__name = name
std = student('liuzhen')
print(std.get_name())

#方法二，用@语法糖，使得我们要使用set get功能时只需要通过.xx的形式即可
class Student():
    def __init__(self, body):
        self.__name = body
    @property
    def name(self):
        return self.__name
    @name.setter # 和方法名要相同
    def name(self, name):
        self.__name = name
std1 = Student('zhendada')
print(std1.name)




