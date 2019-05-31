#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 16:20
# @Author  : 抑郁小六
# @File    : VIP免费.py
# @Software: PyCharm
# @Site    : 
# @Desc    :

import re
import requests
import tkinter as tk
import webbrowser
respons = requests.get('http://www.qmaile.com/')
respons.encoding = respons.apparent_encoding
responsd = respons.text
#  print(responsd)
reg = re.compile('<option value="(.*?)" selected="">') # *匹配前面出现0次或者无限多次
res = re.findall(reg, responsd)
print(res)
one = res[0]
two = res[1]
three = res[2]
four = res[3]
five = res[4]
#six = res[5]
root = tk.Tk()
root.title('Vip电影播放')
root.geometry('500x250') # 宽*长
l1 = tk.Label(root, text='播放接口:', font=("Arial", 12),)  # bg='pink'height=3
l1.grid(row=0, column=0)
l2 = tk.Label(root, text='播放链接:', font=("Arial", 12),)
l2.grid(row=6, column=0)
t1 = tk.Entry(root, text='', width=50)
t1.grid(row=6, column=1)
var = tk.StringVar()   # StringVar是Tk库内部定义的字符串变量类型，在这里用
# 于管理部件上面的字符；不过一般用在按钮button上
r1 = tk.Radiobutton(root, text='播放接口1', variable=var, value=one,)
r1.grid(row=0, column=1)
r2 = tk.Radiobutton(root, text='播放接口2', variable=var, value=two,)
r2.grid(row=1, column=1)
r3 = tk.Radiobutton(root, text='播放接口3', variable=var, value=three,)
r3.grid(row=2, column=1)
r4 = tk.Radiobutton(root, text='播放接口4', variable=var, value=four,)
r4.grid(row=3, column=1)
r5 = tk.Radiobutton(root, text='播放接口5', variable=var, value=five,)
r5.grid(row=4, column=1)
# r6 = tk.Radiobutton(root, text='播放接口6', variable=var, value=six,)
# r6.grid(row=5, column=1)
def bf():
 webbrowser.open(var.get()+t1.get())
b1 = tk.Button(root,text='播放',font=("Arial",12), width=8,command=bf)
b1.grid(row=7, column=1)
def del_text():
 t1.delete(0, 'end')
b2 = tk.Button(root,text='清除',font=("Arial",12), width=8,command=del_text)
b2.grid(row=8, column=1)
root.mainloop()
