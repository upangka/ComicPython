import pygame

from entities import Player
from settings import GameConfig


class GameEngine:
    """游戏主引擎 - 管理游戏生命周期、事件循环、渲染（门面模式）"""

    def __init__(self, config: GameConfig):
        self._running = True
        self.config = config
        self._init_pygame()
        self._init_sprite()

    def _init_pygame(self):
        """初始化 Pygame"""
        pygame.init()
        self.screen = pygame.display.set_mode(
            self.config.SCREEN.get_size()
        )
        pygame.display.set_caption(self.config.WINDOW_TITLE)

    def _init_sprite(self):
        """初始化游戏精灵"""
        self.player = Player(
            'Player.png',
            self.config.SCREEN_WIDTH,
            self.config.SCREEN_HEIGHT
        )

    def _init_resources(self):
        pass

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

    def _render(self):
        pygame.display.update()

    def run(self):
        while self._running:
            self._process_events()
            self._render()
