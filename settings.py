#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 14:00
# @Author  : name
# @File    : settings.py

class Settings():
    '''存储游戏的所有设置的类'''
    def __init__(self):
        '''初始化的游戏设置'''
        # 屏幕设置
        self.screen_width=1200
        self.screen_height=600
        self.bg_color=(255,255,255)
        # 设置飞船移动速度
        self.ship_speed_factor=1.5
        # 设置飞船命数
        self.ship_limit = 3
        # 子弹设置
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        #self.bullet_color=(255,0,0)
        self.bullets_allowed = 20 #限制子弹数目
        # 外星人设置
        self.alien_speed_factor = 0.3 #左右移速度
        self.fleet_drop_speed = 2  #向下移速度
        #fleet_direction为1表示向右，-1表示向左
        self.fleet_direction = 1
