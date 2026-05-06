import logging

import pygame

from entities import (
    Player,
    Enemy
)
from settings import GameConfig
from .state import GameStateManager

logger = logging.getLogger(__name__)


class GameEngine:
    """游戏主引擎 - 管理游戏生命周期、事件循环、渲染（门面模式）"""

    def __init__(self):
        pygame.init()
        self._running = True
        self.config = GameConfig.from_bg_image("Road.png")
        self._init_pygame()
        self._init_sprite()
        self._st_mgr = GameStateManager(self)

    def _init_pygame(self):
        """初始化 Pygame"""
        self.screen = pygame.display.set_mode(
            self.config.SCREEN.get_size()
        )
        pygame.display.set_caption(self.config.WINDOW_TITLE)

    def _init_sprite(self):
        """初始化游戏精灵"""
        self.all_sprites = pygame.sprite.Group()

        self.player = Player(
            self.config.PLAYER_IMG,
            self.config.SCREEN_WIDTH,
            self.config.SCREEN_HEIGHT
        )

        enemy = Enemy("Enemy.png", self.config.SCREEN_WIDTH)

        self.all_sprites.add(self.player)
        self.all_sprites.add(enemy)

    def _init_resources(self):
        # 管理所有精灵
        self.all_sprites = pygame.sprite.Group()
        pass

    def _process_sys_events(self):
        """处理（消费）游戏系统事件,不然主屏幕会卡住"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

    def _render(self):
        self.screen.blit(self.config.SCREEN, (0, 0))
        # 绘制所有精灵 比如画一个玩家 self.screen.blit(self.player.image, self.player.rect)
        # group封装了统一处理
        self.all_sprites.draw(self.screen)
        pygame.display.update()

    def run(self):
        while self._running:
            try:
                self._process_sys_events()
                keys = pygame.key.get_pressed()
                self._st_mgr.handle_keypress(keys)
                self._render()
            except Exception as e:
                logger.error(f"游戏异常: {str(e)}")

        print("游戏结束")

    def update_sprites(self):
        # logger.info("更新精灵")
        ...
