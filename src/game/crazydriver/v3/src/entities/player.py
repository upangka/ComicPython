from dataclasses import dataclass,astuple

from entities import BaseEntity
from resources import resources


@dataclass(frozen=True)
class PlayerInput:
    move_left: bool
    move_right: bool
    paused: bool = False

    def __iter__(self):
        return iter(astuple(self))


class Player(BaseEntity):
    """玩家类，负责玩家移动和渲染"""

    def __init__(self, img_name: str, screen_width: int, screen_height: int):
        image = resources.load_image(img_name)
        # 初始位置底部居中
        center = (screen_width // 2, screen_height - image.get_rect().height // 2)
        super().__init__(
            image=image,
            center=center
        )
        self.screen_width = screen_width

    def update(self, *, player_input: PlayerInput, speed: int):
        """更新玩家位置"""
        move_left,move_right,paused = player_input
        if not paused:
            if move_left:
                self.rect.x = max(0, self.rect.x - speed)
            if move_right:
                self.rect.x = min(self.screen_width - self.rect.width, self.rect.x + speed)


