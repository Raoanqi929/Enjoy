#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 21:54
# @Author  : name
# @File    : game_stats.py

class GameStats():
    '''跟踪游戏的统计信息'''
    def __init__(self,ai_settings):
        '''初始化统计信息'''
        self.ai_settings=ai_settings
        self.reset_stats()
        # 游戏启动前是非活动的
        self.game_active = False

    def reset_stats(self):
        '''初始化在游戏进行期间可能变化的统计信息:重置飞船命数'''
        self.ships_left = self.ai_settings.ship_limit
        #self.score = 0


