import random

from entities import BaseEntity
from resources import resources


class Enemy(BaseEntity):
    """敌人类，负责敌人移动和渲染"""

    def __init__(self, img_name: str, screen_width: int, screen_height: int):
        image = resources.load_image(img_name)

        def _generate_random_position():
            """
            生成器函数：持续产生敌人的随机初始位置
            
            Yields:
                tuple: (x坐标, y坐标)，其中x在屏幕宽度范围内随机，y为图像高度的一半
            """
            low_val = 0
            max_val = screen_width - image.get_rect().width
            while True:
                yield random.randrange(low_val, max_val), image.get_rect().height // 2

        self._generate_pos = _generate_random_position()
        self.screen_width = screen_width
        self.screen_height = screen_height
        super().__init__(
            image=image,
            center=next(self._generate_pos)
        )

    def update(self, *, speed: int):
        self.rect.y += speed
        if self.rect.y > self.screen_height:
            self.reset()

    def reset(self):
        self.rect.center = next(self._generate_pos)
