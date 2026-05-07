import random

from entities import BaseEntity
from resources import resources


class Enemy(BaseEntity):
    """敌人类，负责敌人移动和渲染"""

    def __init__(self, img_name: str, screen_width: int):
        image = resources.load_image(img_name)
        # 随机生成位置
        low = 0
        max = screen_width - image.get_rect().width
        super().__init__(
            image=image,
            center=(random.randrange(low, max), image.get_rect().height // 2)
        )

    def update(self,*,speed: int):
        ...
