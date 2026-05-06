import pygame

from resources import resources


class Player(pygame.sprite.Sprite):
    """玩家类，负责玩家移动和渲染"""

    def __init__(self, img_name: str, screen_width: int, screen_height: int):
        self.img = resources.load_image(img_name)
        self._rect = self.img.get_rect()
        # 初始位置底部居中
        self._rect.center = (screen_width // 2, screen_height - self.rect.height // 2)
        self.screen_width = screen_width

    @property
    def rect(self):
        return self._rect
