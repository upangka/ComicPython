"""玩家类模块"""
from dataclasses import dataclass
import pygame
from .base import BaseEntity


@dataclass
class PlayerInput:
    """
    玩家输入数据传输对象
    
    封装玩家的输入状态，便于传递和处理
    """
    move_left: bool = False
    move_right: bool = False
    pause: bool = False


class Player(BaseEntity):
    """
    玩家类
    
    控制玩家赛车的移动和边界检测
    """
    
    def __init__(self, image: pygame.Surface, screen_width: int, screen_height: int):
        """
        初始化玩家
        
        Args:
            image: 玩家赛车图像
            screen_width: 屏幕宽度
            screen_height: 屏幕高度
        """
        # 初始位置：底部中央
        initial_position = (screen_width // 2, screen_height - image.get_height() // 2)
        super().__init__(image, initial_position)
        
        self.screen_width = screen_width
        self.screen_height = screen_height
    
    def update(self, player_input: PlayerInput, speed: int):
        """
        更新玩家位置
        
        Args:
            player_input: 玩家输入状态
            speed: 移动速度
        """
        # 处理左右移动
        if player_input.move_left:
            self.rect.move_ip(-speed, 0)
        
        if player_input.move_right:
            self.rect.move_ip(speed, 0)
        
        # 边界限制：确保玩家在屏幕内
        self._clamp_to_screen()
    
    def _clamp_to_screen(self):
        """将玩家限制在屏幕范围内"""
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
    
    def reset(self):
        """重置玩家到初始位置"""
        self.rect.center = (
            self.screen_width // 2,
            self.screen_height - self.image.get_height() // 2
        )
