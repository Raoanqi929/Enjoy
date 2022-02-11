#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 14:10
# @Author  : name
# @File    : ship.py

import pygame

class Ship():
    def __init__(self,screen,ai_settings):
        '''初始化飞船并设置其初始位置'''
        self.screen=screen
        # 加载飞船图标并获取其“外接矩形”
        self.image=pygame.image.load('images/baibai.bmp') #返回一个飞船的 surface
        self.rect=self.image.get_rect() #把图片装进矩形
        self.screen_rect=screen.get_rect()
        self.ai_settings = ai_settings
        # 将新飞船放在屏幕底部中间(或屏幕中央)
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        #self.rect.bottom=self.screen_rect.bottom/2
        #飞船左右上下移动标志
        self.moving_right=False
        self.moving_left = False
        self.moving_top= False
        self.moving_bottom = False
        # 飞船坐标
        self.center=float(self.rect.centerx) #
        self.bottom=float(self.rect.bottom)


    def update(self):
        '''这里更新的是self.center而不是self.rect.centerx，因为后者仅保存整数部分'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center-=self.ai_settings.ship_speed_factor
        if self.moving_top and self.rect.top > 0:
            self.bottom-=self.ai_settings.ship_speed_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.bottom+=self.ai_settings.ship_speed_factor
         #更新飞船x坐标值
        self.rect.centerx=self.center
        self.rect.bottom=self.bottom

    def center_ship(self):
        '''让飞船回到原中心位置'''
        self.center = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom
        #self.bottom = self.screen_rect.bottom/2

    def blitme(self):
        '''将飞船绘制到屏幕指定位置上'''
        self.screen.blit(self.image,self.rect)
