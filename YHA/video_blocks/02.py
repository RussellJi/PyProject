# -*- coding: UTF-8 -*-
# font.py

# 导入需要的模块
import pygame, sys
from pygame.locals import *

# 初始化pygame
pygame.init()

# 设置窗口的大小，单位为像素
screen = pygame.display.set_mode((500, 400))

# 设置窗口的标题
pygame.display.set_caption('Font')

# 定义颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

# 通过字体文件获得字体对象
fontObj = pygame.font.Font('仿宋_GB2312.ttf', 50)

# 配置要显示的文字
textSurfaceObj = fontObj.render('Pygame', True, BLUE, GREEN)

# 获得要显示的对象的rect
textRectObj = textSurfaceObj.get_rect()

# 设置显示对象的坐标
textRectObj.center = (250, 200)

# 设置背景
screen.fill(WHITE)

# 绘制字体
screen.blit(textSurfaceObj, textRectObj)

# 程序主循环
while True:

    # 获取事件
    for event in pygame.event.get():
        # 判断事件是否为退出事件
        if event.type == QUIT:
            # 退出pygame
            pygame.quit()
            # 退出系统
            sys.exit()

    # 绘制屏幕内容
