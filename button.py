#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 22:51
# @Author  : name
# @File    : button.py

import pygame.font

class Button():
    def __init__(self,ai_settings,screen,msg):
        '''初始化按钮属性(msg是写在按钮上的文本)'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 设置按钮尺寸等属性
        self.width,self.height= 120,50
        self.button_color =(255,105,180)
        self.text_color = (255,255,255)
        self.font= pygame.font.SysFont(None,36)
        #创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.centerx=self.screen_rect.centerx
        #按钮标签只需创建一次
        self.preg_msg(msg)
        """# 用特定的图标表示按钮
        self.image = pygame.image.load("images/button.bmp")
        self.rect = self.image.get_rect()
        self.rect.center=self.screen_rect.center"""

    def preg_msg(self,msg):
        '''将msg文本信息渲染成图像，并使其在按钮上居中'''
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''绘制一个用颜色填充的按钮，再绘制文本'''
        self.screen.fill(self.button_color,self.rect) #相当于在制定的rect位置填充颜色
        self.screen.blit(self.msg_image,self.msg_image_rect)
        """self.screen.blit(self.image,self.rect)"""

