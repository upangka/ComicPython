import random
from typing import overload

from entities import BaseEntity
from resources import resources


class Enemy(BaseEntity):
    """敌人类，负责敌人移动和渲染"""

    def __init__(self, img_name: str, screen_width: int, screen_height: int, speed_multiplier: float = 1.0):
        """
         Args:
            img_name: 敌人图片
            screen_width: 宽度
            screen_height: 高度
            speed_multiplier: 速度倍率（默认1.0）
        """

        image = resources.load_image(img_name)
        super().__init__(image=image)

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.multiplier = speed_multiplier

        def _generate_random_center():
            """
            生成器函数：持续产生敌人的随机初始位置

            Yields:
                tuple: (x坐标, y坐标)，其中x在屏幕宽度范围内随机，y为图像高度的一半
            """
            half_w = image.get_width() // 2
            max_val = screen_width - half_w
            while True:
                yield random.randrange(half_w, max_val), 0

        self._generate_center = _generate_random_center()
        # 防重叠：延迟激活
        self.spawn_delay = 0
        self.active = True
        self.reset()

    def update(self, *, speed: int) -> bool:
        """
           向下移动敌人
           Args:
               speed: 基础移动速度
           Returns:
               True 表示敌人已超出屏幕底部（可计分）
       """
        # 延迟激活
        if not self.active:
            self.spawn_delay -= 1
            if self.spawn_delay <= 0:
                self.active = True
            return False

        self.rect.y += speed * self.multiplier
        return self.rect.y > self.screen_height

    def reset(self):
        """重置敌人到顶部随机位置（不检查重叠，由引擎处理）"""
        self.rect.center = next(self._generate_center)

        # 重置时添加随机延迟
        self.spawn_delay = random.randint(0, 30)
        self.active = False

    def try_non_overlap_position(self, existing_enemies: 'pygame.sprite.Group',
                                 min_distance: int = 80) -> bool:
        """
        尝试找到不与其他敌人重叠的位置（最多尝试15次）
        Args:
            existing_enemies: 现有的敌人精灵组
            min_distance: 最小X轴距离
        Returns:
            True 表示找到了不重叠的位置
        """

        overlap = True
        for _ in range(30):
            self.rect.center = next(self._generate_center)
            for enemy in existing_enemies:
                # 经过调试250之内的都需要比较，不然会出现重叠
                if enemy is not self and enemy.rect.top < 250:
                    if abs(enemy.rect.x - self.rect.x) > min_distance:
                        overlap = True
                        break

        if not overlap:
            return True

        return False