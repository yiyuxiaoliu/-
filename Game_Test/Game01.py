#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 
# @Desc    :
# 定义一个装备类 equipment：
# 		成员变量：名字、防御defense
# 		构造方法：无参构造方法，带参构造方法
# 		成员方法；设置名字（set方法）、获得名字（get方法）、设置防御、获得防御。
# 	定义一个武器类arms
# 		成员变量：名字、攻击attack
# 		构造方法：无参构造方法，带参构造方法
# 		成员方法；设置名字（set方法）、获得名字（get方法）、设置伤害、获得伤害。
# 	定义一个角色类role
# 		成员变量：名字、血量Blood 、伤害Hurt
# 		成员方法：设置名字（set方法）、获得名字（get方法）、设置防御、获得伤害，设置血量，获得血量。
# 		成员方法：穿装备，穿武器。
# 	定义一个动作类action
# 		成员变量：距离distance
# 		成员变量：移动的距离
# 		成员方法：前进（通过距离来判断是否遇到BOSS）
# 		成员方法：战斗（英雄或BOSS血量为0时结束）
# 	定义一个公共类public
# 		main方法，创建对象，执行方法，最终能玩游戏。

class equipment():

