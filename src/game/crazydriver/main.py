import sys

import pygame
from pygame.locals import *  # pygame所有常量

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
# 管理帧率
clock = pygame.time.Clock()
# 每秒60帧
clock.tick(60)
pygame.display.set_caption('赛车游戏')
# 游戏区域surface，显示窗口
screen = pygame.display.set_mode((500, 800))
# 设置背景颜色
screen.fill(WHITE)
# 刷新
pygame.display.update()

# 主循环
while True:
    # 事件检查
    for event in pygame.event.get():
        print(type(event), event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # 刷新
    pygame.display.update()
