import pygame

from resources import resources
from settings import Color


class GameOverTip:
    """结束语言"""
    _default_font: str = None
    _default_font_size: int = 25

    """游戏结束提示"""

    def __init__(self, *, text: str, font_name: str = None, center: tuple, font_size: int = None, color: Color = Color.WHITE):
        font_name = font_name or self._default_font
        font_size = font_size or self._default_font_size
        font = resources.load_font(font_name, font_size)
        self.surface = font.render(text, True, color)
        self.rect = self.surface.get_rect(center=center)

    def render(self, screen: pygame.Surface):
        """渲染"""
        screen.blit(self.surface, self.rect)

    @classmethod
    def config(cls, font: str = None, font_size: int = 25):
        """配置字体相关"""
        cls._default_font = font
        cls._default_font_size = font_size
