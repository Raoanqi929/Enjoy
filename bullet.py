#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 16:17
# @Author  : name
# @File    : bullet.py

import pygame
from pygame.sprite import  Sprite

class Bullet(Sprite):
    '''一个对飞船发射的子弹进行管理的类'''
    def __init__(self,ai_settings,screen,ship):
        '''在飞船的位置插件一个子弹对象'''
        super().__init__() #继承Sprite
        self.screen=screen
        #在(0,0)处穿件一个表示子弹的形状，在设置正确位置
        self.image=pygame.image.load('images/heart.bmp') #返回一个心形子弹surface
        #self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect = self.image.get_rect()  # 把图片装进矩形
        self.rect.centerx = ship.rect.centerx #子弹的x坐标
        self.rect.top = ship.rect.top #子弹y坐标
        #存储用小数表示的子弹位置
        self.y=float(self.rect.y) #为了小数表示而产生
        #self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        '''向上移动子弹'''
        #更新表示子弹位置的值（是小数）
        self.y-=self.speed_factor
        #跟新表示子弹的rect的位置
        self.rect.y=self.y

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        #pygame.draw.rect(self.screen,self.color,self.rect)
        self.screen.blit(self.image, self.rect)



