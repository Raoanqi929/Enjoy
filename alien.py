#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 17:47
# @Author  : name
# @File    : alien.py

import pygame
from pygame.sprite import  Sprite

class Alien(Sprite):
    '''表示单个外星人的类'''
    def __init__(self,ai_settings,screen,alien_type):
        '''初始化外星人并设置其起始位置'''
        super().__init__() #继承Sprite
        self.screen=screen
        self.ai_settings=ai_settings
        #加载外星人图片并获取其rect属性（这里设置4种类型的外星人）
        if alien_type == "lu":
            self.image = pygame.image.load('images/lu.bmp')
        elif alien_type == "zuo":
            self.image = pygame.image.load('images/zuo.bmp')
        elif alien_type == "mo":
            self.image = pygame.image.load('images/mo.bmp')
        elif alien_type == "xia":
            self.image = pygame.image.load('images/xia.bmp')
        self.rect=self.image.get_rect()
        #设置每个外星人初始位置（左上角）
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #存储外星人准确位置
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        '''如果外星人位于屏幕边缘，返回True'''
        screen_rect=self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True #
        elif self.rect.left <=0:
            return True

    def update(self):
        '''向右/左移动外星人'''
        self.x+= (self.ai_settings.alien_speed_factor*
                  self.ai_settings.fleet_direction)
        self.rect.x=self.x

