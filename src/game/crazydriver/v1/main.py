import random
import sys
import time

import pygame
from pygame import Surface
from pygame.locals import *

# from resources import *


# 常量
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 移动速度 5像素
move_speed = 5
temp_move_speed = 0
max_speed = 10

score = 0
paused = False

# 资源路径

GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGES_FOLDER = os.path.join(GAME_ROOT_FOLDER, 'images')

IMG_ROAD_FILE_PATH = os.path.join(IMAGES_FOLDER, 'Road.png')
IMG_PLAYER_FILE_PATH = os.path.join(IMAGES_FOLDER, 'Player.png')
IMG_ENEMY_FILE_PATH = os.path.join(IMAGES_FOLDER, 'Enemy.png')
IMG_ENEMY2_FILE_PATH = os.path.join(IMAGES_FOLDER, 'Enemy2.png')
IMG_ENEMY3_FILE_PATH = os.path.join(IMAGES_FOLDER, 'Enemy3.png')

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
    def __init__(self, enemy: Surface):
        super().__init__()
        self.image = enemy
        self.surf = pygame.surface.Surface(enemy.get_size())
        self.rect = self.surf.get_rect(
            center=(random.randint(self.image.get_width() // 2, IMG_ROAD.get_width() - self.image.get_width() // 2), 0))

    def reset(self):
        self.rect.center = (
            random.randint(self.image.get_width() // 2, IMG_ROAD.get_width() - self.image.get_width() // 2), 0)


class GameOverTip(pygame.sprite.Sprite):
    text_size = 40
    font_path = os.path.join(GAME_ROOT_FOLDER, 'fonts', '字心坊小呀小布丁.TTF')

    def __init__(self, tip: str):
        super().__init__()
        self.font_style = pygame.font.Font(GameOverTip.font_path, GameOverTip.text_size)
        self.surf = self.font_style.render(tip, True, RED)
        self.rect = self.surf.get_rect(center=(IMG_ROAD.get_width() // 2, IMG_ROAD.get_height() // 2))


def game_over():
    print("游戏结束")
    tip = GameOverTip('游戏结束')
    screen.fill(BLACK)
    screen.blit(tip.surf, tip.rect)
    pygame.display.update()

    player.kill()
    enemy.kill()

    time.sleep(5)
    pygame.quit()
    sys.exit()


player = Player()
enemy = Enemy(IMG_ENEMY)
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
    # 事件检查
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if pygame.sprite.collide_rect(player, enemy):
        game_over()

    # 加到主surface上
    screen.blit(IMG_ROAD, (0, 0))
    screen.blit(player.image, player.rect)
    screen.blit(enemy.image, enemy.rect)
    pygame.display.set_caption(f'疯狂赛车 得分: {score}')
    
    enemy.rect.move_ip(0, move_speed)
    if enemy.rect.top > IMG_ROAD.get_height():
        enemy.reset()
        score += 1
        if move_speed < max_speed:
            move_speed += 1

    keys = pygame.key.get_pressed()
    if paused:
        if keys[K_SPACE]:
            paused = False
            move_speed = temp_move_speed
    else:
        if (keys[K_LEFT] or keys[K_a]) and player.rect.left > 0:
            player.rect.move_ip(-move_speed, 0)
            if player.rect.left < 0:
                player.rect.left = 0
        if (keys[K_RIGHT] or keys[K_d]) and player.rect.right < IMG_ROAD.get_width():
            player.rect.move_ip(move_speed, 0)
            if player.rect.right > IMG_ROAD.get_width():
                player.rect.right = IMG_ROAD.get_width()

        if keys[K_SPACE]:
            paused = True
            temp_move_speed = move_speed
            move_speed = 0

    

    # 刷新
    pygame.display.update()
