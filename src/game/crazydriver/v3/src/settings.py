from dataclasses import dataclass, field

import pygame

from resources import resources


@dataclass(frozen=True)
class GameConfig:
    """游戏配置数据类

   使用冻结的数据类（frozen=True）确保配置在运行时不可变，防止意外修改。

   Attributes:
       WINDOW_TITLE: 游戏窗口标题
       FPS: 游戏帧率（每秒帧数）
       INITIAL_SPEED: 游戏初始速度
       MAX_SPEED: 游戏最大速度
       SCREEN_WIDTH: 屏幕宽度（像素），默认值会被动态覆盖
       SCREEN_HEIGHT: 屏幕高度（像素），默认值会被动态覆盖
   """

    # 屏幕尺寸将从背景图片动态获取，这里作为默认值
    SCREEN_WIDTH: int = 500
    SCREEN_HEIGHT: int = 800
    SCREEN: pygame.Surface = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    WINDOW_TITLE: str = '疯狂赛车'
    FPS: int = 60
    INITIAL_SPEED: int = 5
    MAX_SPEED: int = 10

    PLAYER_IMG: str = "Player.png"
    ENEMY_IMG: str = "Enemy.png"

    ENEMY_TYPES: list[tuple[str, float, int]] = field(default_factory=lambda: [
        ('Enemy.png', 1.0, 80),  # 最小间距80px
        ('Enemy2.png', 1.2, 90),  # 最小间距90px（图片更大）
        ('Enemy3.png', 1.5, 100),  # 最小间距100px（图片最大）
    ])

    FONT: str = '字心坊小呀小布丁.TTF'
    FONT_SIZE: int = 25

    @classmethod
    def from_bg_image(cls, img_name: str):
        """根据背景图片动态设置屏幕尺寸大小"""
        img = resources.load_image(img_name)
        return cls(
            SCREEN_WIDTH=img.get_width(),
            SCREEN_HEIGHT=img.get_height(),
            SCREEN=img)


class Color:
    """颜色常量定义
    提供游戏中常用的 RGB 颜色元组。
    Attributes:
        BLACK: 黑色 (0, 0, 0)
        WHITE: 白色 (255, 255, 255)
        RED: 红色 (255, 0, 0)
    """
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
