#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 
# @Desc    : 关联

from locust import HttpLocust, TaskSet, task
import json
from common import readConfig


class UserBehavior(TaskSet):  # 定义用户行为
    def on_start(self):  # 当模拟用户开始执行TaskSet类的时候，on_start方法会被调用
        pass
    def get_headers(self):
　　 """会员登录"""
        headers = {
            "Content-Type": "application/json",
            "channel": "SHOP"
        }
        body = {
            "unionid": readConfig.unionid # 这样使用会报错，没有 common ...
        }
        res = self.client.post('/customers/login', headers=headers, data=json.dumps(body)).text
        assert '成功' in res  # 断言，判断接口返回是否成功
        res = json.loads(res)
        uid = res['data']['uid']
        ukey = res['data']['ukey']
        return [uid, ukey] # 会员登录返回的uid和ukey
    @task(1)
    def members_can_withdraw_account_information(self):  # 一个行为
        """使会员获取会员状态"""
        res = self.get_headers()
        headers = {
            "channel": "SHOP",
            "uid": str(res[0]),
            "ukey": res[1]
        }
        response = self.client.put("/customers/customer_state",
                                   headers=headers).text  # client.get()用于指请求的路径，可加headers,params,body参数;
        assert '成功' in response

    @task(1)
    def get_member_account_withdrawal_details(self):
        """获取会员账户提现明细"""
        res = self.get_headers()
        headers = {
            "channel": "SHOP",
            "uid": str(res[0]),
            "ukey": res[1]
        }
        params = {
            "page": "10",
            "size": "10"
        }
        response = self.client.get("/customers/account/withdraw/log", headers=headers, params=params).text
        assert '成功' in response


class WebsiteUser(HttpLocust):  # 设置性能测试;
    host = "http://dev.sign.lixiaofeng.com"
    task_set = UserBehavior  # 指向一个定义了的用户行为类;
    min_wait = 3000  # 用户执行任务之间等待时间的下界，单位：毫秒;
    max_wait = 6000  # 用户执行任务之间等待时间的上界，单位：毫秒;
