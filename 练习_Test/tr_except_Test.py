#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 
# @Desc    :
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# title = 'adsasd sasd asdas asd'
# asd = title.split()
# print(len(asd))
import unittest
class liuzhen(unittest.TestCase):
    def le(filename):
        try:
             with open(filename) as f_obj:
                 contents = f_obj.read()
        except FileNotFoundError:
              msg = "Sorry, the file " + filename + " does not exist."
              print(msg)
        else:
            #  计算文件大致包含多少个单词
             words = contents.split()
             num_words = len(words)
             print("The file " + filename + " has about " + str(num_words) + " words.")

    fo = 'file.txt'
    le(fo)
unittest.main