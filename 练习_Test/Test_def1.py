#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 
# @Desc    :
#
import webbrowser
from PIL import Image,ImageFilter
# webbrowser.open("https://www.baidu.com/")

im = Image.open(r"C:\Users\lenovo\Desktop\身份证1.jpg")   # 打开jpg图片
im1 = im.filter(ImageFilter.BLUR)    # 增加模糊滤镜
im1.save(r"C:\Users\lenovo\Desktop\身份证2.jpg")