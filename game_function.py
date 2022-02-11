#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 14:44
# @Author  : name
# @File    : game_function.py

import sys
import pygame
import  random
from time import sleep
from bullet import Bullet
from alien import  Alien

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
    '''检查是否有子弹击中外星人：'''
    # 若有，则删除相应子弹及外星人(True,True)【若想能实现一发子弹集中多个外星人z则为(False,True)】
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 当当前批的外星人被消灭，新建一群外星人
    if len(aliens) == 0:
        # 删除现有子弹并新建一群外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def update_bullets(ai_settings,screen,ship,aliens,bullets):
    # 更新子弹的位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():  # 因为下面要对bullets修改，因此用bullets的副本
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检查是否有子弹击中外星人：
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    '''响应飞船撞到外星人'''
    if stats.ships_left > 1: #若飞船还有剩余，则游戏继续
        # ships_left 少1
        stats.ships_left -= 1
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新外星人，并将飞船放回中心原位
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停 1 s
        sleep(1)
    else:   # 否则结束游戏
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    '''检查是否有外星人触碰底端'''
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #若外星人碰到屏幕底端，像ship_hit一样处理
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    '''检查是否有外星人位于屏幕边缘，
       并更新外星人群中所有外星人位置'''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    # 监检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
    # 检查是否有外星人触碰屏幕底端
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
    '''在限制数量内发射一颗子弹'''
    # 创建一颗新子弹，并加入到bullets编组里，如果当前屏幕中存在的子弹数目不超过限制的话
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullets = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullets)

def check_fleet_edges(ai_settings,aliens):
    '''有外星人到达边界时采取向右措施'''
    for alien in aliens.sprites():
        if alien.check_edges(): #如果碰到边界
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    '''将整群外星人下移，并改变他们方向'''
    for alien in aliens.sprites():
        alien.rect.y+= ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*= -1  #改变左右方向

def get_number_aliens_x(ai_settings,alien_width):
    '''计算水平可容纳多少外星人'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    '''计算屏幕垂直可容纳多少行外星人'''
    available_space_y=(ai_settings.screen_height-2*alien_height-ship_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows

def creat_alien(ai_settings,screen,aliens,alien_number,row_number,alien_type):
    '''新建一个外星人'''
    alien = Alien(ai_settings, screen,alien_type)
    alien_width=float(alien.rect.width)*2/3 #外星人之间的间距为一个外星人矩形的宽度
    alien.x = alien_width + 2 * alien_width * alien_number  # 下一个外星人矩形的x坐标
    alien.rect.x = alien.x
    alien_height=float(alien.rect.height/2)
    alien.y=alien_height+2*alien_height*row_number
    alien.rect.y=alien.y
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    '''创建外星人群'''
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距假设为外星人宽度
    alien = Alien(ai_settings, screen,"lu")
    alien_width = float(alien.rect.width)*2/3 #外星人之间横竖间距
    alien_height= float(alien.rect.height/2)
    number_aliens_x=get_number_aliens_x(ai_settings,alien_width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien_height)
    #创建一群外星人
    alien_types = ["lu","zuo","mo","xia"]
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings,screen,aliens,alien_number,row_number,alien_types[random.randint(0,3)])


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''相应按下键盘'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_top = True
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q: #按“Q”退出游戏
        sys.exit()

def check_keyup_events(event, ship):
    '''响应松开键盘'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_top = False
    if event.key == pygame.K_DOWN:
        ship.moving_bottom = False

def check_events(ai_settings,screen,ship,bullets,aliens,stats,play_button):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 检测到关闭游戏窗口
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,ship,aliens,bullets,stats,play_button,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,ship,aliens,bullets,stats,play_button,mouse_x,mouse_y):
    '''玩家单击按钮开始新游戏'''
    # 若鼠标点击到指定位置（play_button的位置）
    button_clicked= play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #隐藏光标
        pygame.mouse.set_visible(False)
        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        #清空外星人和子弹列表
        aliens.empty()
        bullets.empty()
        #创建一群新的外星人，并重置飞船位置
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

def update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button):
    '''更新屏幕上的图像（包括飞船/角色等）'''
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets:
        bullet.draw_bullet()
     # 绘制飞船位置
    ship.blitme()
    # 整群绘制外星人
    aliens.draw(screen)
    # 如果游戏处于非活动状态，绘制play按钮
    if not stats.game_active:
        play_button.draw_button()
    #刷新屏幕
    pygame.display.flip()



