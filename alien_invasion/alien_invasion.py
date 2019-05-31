#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 13:07
# @Author  : 抑郁小六
# @File    : 注册.py
# @Software: PyCharm
# @Site    : 
# @Desc    :
#  我们导入了模块 sys 和 pygame 。模块 pygame 包含开发游戏所需的功能。玩家退出时，我们将使用模块 sys 来退出游戏
import sys
import pygame
from settings import Settings


def run_game():
    #  初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化背景设置
    #  对象 screen 是一个 surface(想当与外表)，用于显示游戏元素。在这个游戏中，每个元素（如外星人或飞船）都是一个 surface
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)))  # 调用 pygame.display.set_mode() 来创建一个名为 screen 的显示窗口，这个游戏的所有图形元素都将在其中绘制。实参 (1200, 800) 是一个元组，指定了游戏窗口的尺寸。通过将这些尺寸值传递给 pygame.display.set_mode() ，我们创建了一个宽 1200 像素、高 800 像素的游戏窗口
    pygame.display.set_caption("Alien Invasion")
    #  设置背景色
    bg_color = (230, 230, 230)
    #  开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 玩家单击游戏窗口的关闭按钮时，将检测到 pygame.QUIT 事件，而我们调用 sys.exit() 来退出游戏
                sys.exit()
        # 每次循环时都重绘屏幕
        screen.fill()
        # 让最近绘制的屏幕可见
        pygame.display.flip()  # 每次执行 while 循环时都绘制一个空屏幕，并擦去旧屏幕

run_game()