#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 13:31
# @Author  : name
# @File    : alien_invasion.py

import pygame
from settings import Settings
from pygame.sprite import Group
from ship import Ship
import game_function as gf
from game_stats import  GameStats
from button import Button

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings() #创建屏幕设设置信息对象
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #设置游戏屏幕尺寸
    pygame.display.set_caption("Alien Invasion") #游戏标题
    #创建Play按钮
    play_button=Button(ai_settings,screen,"Play")
    # 创建一艘飞船
    ship=Ship(screen,ai_settings)
    # 创建一个用于存储子弹的编组
    bullets=Group()
    # 外星人群
    aliens=Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # 创建一个储存游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 开始游戏的主循环
    while True: #该游戏由该一个while循环控制！
        # 监视键盘和鼠标(即玩家操作)事件;
        gf.check_events(ai_settings,screen,ship,bullets,aliens,stats,play_button)
        # 当游戏状态为True才继续更新位置
        if stats.game_active:
            # 更新操作后飞船、子弹位置
            ship.update()
            # 更新子弹位置
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # 更新外星人位置
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 每次循环都重绘屏幕，飞船，子弹，外星人，并刷新屏幕
        gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button)

run_game()
