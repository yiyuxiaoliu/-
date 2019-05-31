#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 10:29
# @Author  : 抑郁小六
# @File    : youkuVIP.py
# @Software: PyCharm
# @Site    : 
# @Desc    :

import requests
from multiprocessing import Pool

def temp1(n):
    # for i in range(n):
    # url = "https://youku.cdn-tudou.com/20180515/5909_07808cae/1000k/hls/f4a95697adb%03d.ts"
    url = "https://vip.okokbo.com/20171230/WGIUsKmD/800kb/hls/zltS5RQ81631%03d.ts" % n
    headers = {
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    print(url)
    r = requests.get(url, headers=headers)
    f = open('./mp4/{}'.format(url[-10:]), 'ab')
    f.write(r.content)
    f.close()


if __name__ == '__main__':

    pool = Pool(20)
    for i in range(1500):
         pool.apply_async(temp1, (i,))

    pool.close()
    pool.join()

# copy /b *.ts new.mp4