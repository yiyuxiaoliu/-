#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 银行取款
# @Desc    :

card1 = "1001"
psd1 = "123456"
balance1 = 10000

card2 = '1002'
psd2 = '123456'
balance2 = 10000

card3 = '1003'
psd3 = '123456'
balance3 = 10000
balance = 0
count = 0
print("欢迎来到不坑你那坑谁银行，办理义务：我是大总裁振大大")
while True:

    nmb = input("请输入银行卡账号：")
    max = input("请输入银行卡密码：")

    if nmb == card1 and max == psd1:
        balance = balance1
        print("卡里余额：",balance)
    elif nmb == card2 and max == psd2:
        balance = balance2
        print("卡里余额：", balance)
    elif nmb == card3 and max == psd3:
        balance = balance3
        print("卡里余额：", balance)
    else:
        count += 1
        if count >= 3:
            print("您已经输错三次，请联系银行工作人员！")
            break
        else:
            print("输入错误，请重新输入")
            continue

    while True:
        money = 0
        duty = str(input("请输入办理的业务：1、存钱；2、取钱； 3、取卡"))
        if duty == "1":
            money = int(input("输入存款金额："))
            if money <= 0:
                print("输入金额请大于零")
            else:
                balance = balance+money
                print("存款成功！存出金额：", money,  "卡里余额为：", balance)
        elif duty == "2":
            mone = int(input("输入取款金额："))
            if mone > money:
                print("余额不足，请重新输入！")
                continue
            else:
                balance = balance - money
                print("取款成功！取出金额：", mone, "卡里余额为：", balance)
        elif duty == "3":
            print("退卡成功！")
            break
        else:
            print("业务输入错误，请重新输入！")
            continue

