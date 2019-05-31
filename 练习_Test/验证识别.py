#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 
# @Desc    :

import pytesseract
from PIL import Image
image = Image.open('test1.jpg')
vcode = pytesseract.image_to_string(image)
print(vcode)