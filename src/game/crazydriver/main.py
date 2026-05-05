import random
import sys

import pygame
from pygame.locals import *

from resources import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 移动速度 5像素
move_speed = 5

# 图片surface
IMG_ROAD = pygame.image.load(IMG_ROAD_FILE_PATH)
IMG_PLAYER = pygame.image.load(IMG_PLAYER_FILE_PATH)
IMG_ENEMY = pygame.image.load(IMG_ENEMY_FILE_PATH)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = IMG_PLAYER
        self.surf = pygame.surface.Surface(IMG_PLAYER.get_size())
        self.rect = self.surf.get_rect(center=(250, 800 - 80 / 2))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = IMG_ENEMY
        self.surf = pygame.surface.Surface(IMG_ENEMY.get_size())
        self.rect = self.surf.get_rect(
            center=(random.randint(IMG_ENEMY.get_width() // 2, 800 - IMG_ENEMY.get_width() // 2), 0))

    def reset(self):
        self.rect.center = (random.randint(IMG_ENEMY.get_width() // 2, 800 - IMG_ENEMY.get_width() // 2), 0)


player = Player()
enemy = Enemy()
pygame.init()
# 管理帧率
clock = pygame.time.Clock()
# 每秒60帧
clock.tick(60)
pygame.display.set_caption(f'{IMG_PLAYER.get_size()}')

# 游戏区域surface，显示窗口
screen = pygame.display.set_mode(IMG_ROAD.get_size())
# 设置背景颜色
screen.fill(WHITE)
# 刷新
pygame.display.update()

# 主循环
while True:
    # 加到主surface上
    screen.blit(IMG_ROAD, (0, 0))
    screen.blit(player.image, player.rect)
    screen.blit(enemy.image, enemy.rect)
    enemy.rect.move_ip(0, move_speed)
    if enemy.rect.top > IMG_ROAD.get_height():
        enemy.reset()
    # 事件检查
    for event in pygame.event.get():
        print(type(event), event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # 刷新
    pygame.display.update()
