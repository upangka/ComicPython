import pygame

from settings import GameConfig


class GameEngine:
    """游戏主引擎 - 管理游戏生命周期、事件循环、渲染（门面模式）"""

    def __init__(self, config: GameConfig):
        self._running = True
        self.config = config
        # self._init_pygame()


    def _init_pygame(self):
        pygame.init()

    def run(self):
        while self._running:
            pass
