from entities import BaseEntity
from resources import resources


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
