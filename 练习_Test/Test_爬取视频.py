#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 
# @Desc    :
import requests
import re
import os
import time
from urllib.request import urlretrieve  #下载模块
def video_DL(url):
    #添加请求头
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"}
    #获取网页源代码
    #url = "http://www.pearvideo.com/category_59"
    response = requests.get(url,headers = header)
    html = response.text
    # 正则匹配获取视频ID
    reg = '<a href="(.*?)" class="vervideo-lilink actplay">'
    video_id = re.findall(reg, html)
    video_url = []
    for i in video_id:
        #拼接url地址
        video_html = "http://www.pearvideo.com/{}".format(i)
        video_url.append(video_html)
    for j in video_url:
        #获取视频播放地址
        purl = requests.get(j).text
        req = 'srcUrl="(.*?)"'
        purl_1 = re.findall(req,purl)
        #获取视频标题
        res = '<h1 class="video-tt">(.*?)</h1>'
        video_name = re.findall(res,purl)
        # print(video_name[0])
        #下载视频
        print("正在下载视频：%s"%video_name[0])
        path = "video"
        #判断当前目录有没有video文件
        if path not in os.listdir():
            os.mkdir(path)
        #下载视频
        urlretrieve(purl_1[0],path+"/%s.mp4"%video_name[0])
def download():
    #动态加载地址
    #http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=59&start=24
    #http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=59&start=36
    n = 12
    while True:
        if n > 48:
            #结束函数
            return
        url = "http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=59&start={}".format(n)
        n += 12
        time.sleep(1)
        #调用上面写好的下载函数
        video_DL(url)
download()