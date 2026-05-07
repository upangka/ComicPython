from abc import ABC,abstractmethod

import pygame


class BaseEntity(pygame.sprite.Sprite, ABC):
    """游戏精灵基类
    满足pygame.sprite.Sprite的条件:

        The Group.draw() method requires that each Sprite have a Surface.image attribute
        and a Surface.rect.
    """

    def __init__(self, *, image: pygame.Surface, center: tuple):
        """精灵类的要求必须要有image和rect属性"""
        self.image = image
        self.rect = self.image.get_rect(center=center)
        super().__init__()

    @abstractmethod
    def update(self,*args,**kwargs):
        """更新精灵"""
        ...