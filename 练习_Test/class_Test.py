#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 
# @Desc    :
#  小狗类：
# class Dog():
#     """ 一次模拟小狗的简单尝试 """
#     def __init__(self, name, age):
#         """ 初始化属性 name 和 age"""
#         self.nam = name
#         self.age = age
#     def sit(self):
#         """ 模拟小狗被命令时蹲下 """
#         print(self.nam.title() + " 狗子蹲下.")
#     def roll_over(self):
#         """ 模拟小狗被命令时打滚 """
#         print(self.nam.title() + " 狗子打滚!")
#
#
# my_dog = Dog('willie', 6)
# your_dog = Dog('lucy', 3)
# print("这是我的傻狗叫： " + my_dog.nam.title() + ".")
# print("这是我的傻狗，今年" + str(my_dog.age) + " years old.")
# my_dog.sit()
# print("\n这是我的傻狗叫： " + your_dog.nam.title() + ".")
# print("这是我的傻狗，今年 " + str(your_dog.age) + " years old.")
# your_dog.sit()

# #  餐馆类：
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):  # 方法 __init__() 接受这些形参的值，并将它们存储在根据这个类创建的实例的属性中
#         self.name = restaurant_name
#         self.type = cuisine_type
#         self.odometer = 0
#     def describe_restaurant(self):
#
#         print("这个餐馆叫：" + self.name.title() +","+ "名字叫：" + self.type.title())
#     def open_restaurant(self):
#         last_name = str(self.name.title) + str(self.type.title())
#         return last_name
#     def read_odometer(self, oliens):
#         self.odometer+= oliens
#         print(self.odometer)
#
#
# class Restaurant():
#     restaurant = Restaurant('好友来', '张三')
#     print('这是：'+ restaurant.name)
#     print('名称:'+ restaurant.type)
#     restaurant.describe_restaurant()
#     print(restaurant.open_restaurant())
#     restaurant.read_odometer(20)
#     restaurant.read_odometer(30)

# 继承
class Car():
    """ 一次模拟汽车的简单尝试 """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
             print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
            self.odometer_reading += miles

# class ElectricCar(Car):
#     """ 电动汽车的独特之处 """
#     def __init__(self, mak, mode, yea):
#         """ 初始化父类的属性 """
#         super().__init__(mak, mode, yea)
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())

class liuzhen(Car):
    def __init__(self, d, ad, a):
        super().__init__(self, d ,ad ,a)
