#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 8:53
# @Author  : 抑郁小六
# @File    : 滚动条.py
# @Software: PyCharm
# @Site    : 
# @Desc    :

from selenium import webdriver
import time
# 访问百度
driver = webdriver.Chrome('C:\chromedriver')
driver.get("http://www.baidu.com")
# 搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
# 将页面滚动条拖到底部
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)
# 将滚动条移动到页面的顶部
js = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(3)
driver.quit()

# 第二种场景（定位到元素的 id）
# js="var q=document.getElementById('id').scrollTop=10000"
# driver.execute_script(js)
