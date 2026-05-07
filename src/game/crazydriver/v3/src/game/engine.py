import logging

import pygame
from pygame.locals import *

from entities import (
    Player,
    Enemy
)
from entities.player import PlayerInput
from settings import GameConfig
from .state import (GameStateManager, GameState)
from .score import ScoreManager
from .util import check_player_enemy_collision

logger = logging.getLogger(__name__)


class GameEngine:
    """游戏主引擎 - 管理游戏生命周期、事件循环、渲染（门面模式）"""

    def __init__(self):
        pygame.init()
        self._running = True
        self.config = GameConfig.from_bg_image("Road.png")
        self._current_speed = self.config.INITIAL_SPEED
        self._init_pygame()
        self._init_sprite()
        self._st_mgr = GameStateManager(self)
        self.score_mgr = ScoreManager()
        # 帧率控制
        self.clock = pygame.time.Clock()

    def _init_pygame(self):
        """初始化 Pygame"""
        self.screen = pygame.display.set_mode(
            self.config.SCREEN.get_size()
        )
        pygame.display.set_caption(self.config.WINDOW_TITLE)

    def _init_sprite(self):
        """初始化游戏精灵"""
        # 管理所有精灵
        self.all_sprites = pygame.sprite.Group()
        # 单独管理敌人
        self.enemies = pygame.sprite.Group()

        self.player = Player(
            self.config.PLAYER_IMG,
            self.config.SCREEN_WIDTH,
            self.config.SCREEN_HEIGHT
        )

        self.enemy = Enemy(
            "Enemy.png",
            self.config.SCREEN_WIDTH,
            self.config.SCREEN_HEIGHT
        )

        self.enemies.add(self.enemy)
        self.all_sprites.add(self.player, self.enemy)

    def _init_resources(self):

        pass

    def _process_sys_events(self):
        """处理（消费）游戏系统事件,不然主屏幕会卡住"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

    def _render(self):
        # 绘制背景
        self.screen.blit(self.config.SCREEN, (0, 0))
        # 绘制所有精灵 比如画一个玩家 self.screen.blit(self.player.image, self.player.rect)
        # group封装了统一处理
        self.all_sprites.draw(self.screen)
        # 得分
        pygame.display.set_caption(f"{self.config.WINDOW_TITLE}  得分: {self.score_mgr.score}")
        pygame.display.update()

    def run(self):
        while self._running:
            try:
                # 添加帧率限制确保游戏运行稳定
                self.clock.tick(self.config.FPS)
                self._process_sys_events()
                keys = pygame.key.get_pressed()
                self._st_mgr.handle_keypress(keys)
                self._render()
            except Exception as e:
                logger.error(f"游戏异常: {str(e)}")

        print("游戏结束")

    def update_sprites(self):
        """更新精灵"""
        keys = pygame.key.get_pressed()
        play_input = PlayerInput(
            move_left=keys[K_LEFT] or keys[K_a],
            move_right=keys[K_RIGHT] or keys[K_d],
            paused=self._st_mgr.current_state == GameState.PAUSED
        )
        self.player.update(
            player_input=play_input,
            speed=self._current_speed
        )

        for enemy in self.enemies:
            if self.enemy.update(speed=self._current_speed):
                self.score_mgr.add_score(points=1)
                logger.info(f"得分: {self.score_mgr}")

        if check_player_enemy_collision(self.player, self.enemies):
            self._game_over()

    def _game_over(self):
        self._running = False



