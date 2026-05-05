"""游戏实体基类 - 使用抽象基类定义通用接口"""
from abc import ABC, abstractmethod
import pygame


class BaseEntity(pygame.sprite.Sprite, ABC):
    """
    游戏实体基类
    
    所有游戏实体（玩家、敌人等）都应继承此类
    使用抽象方法强制子类实现必要的功能
    """
    
    def __init__(self, image: pygame.Surface, position: tuple):
        """
        初始化实体
        
        Args:
            image: 实体的图像表面
            position: 实体的初始位置 (x, y)
        """
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=position)
    
    @abstractmethod
    def update(self, *args, **kwargs):
        """
        更新实体状态
        
        子类必须实现此方法来定义实体的更新逻辑
        """
        pass
    
    @abstractmethod
    def reset(self, *args, **kwargs):
        """
        重置实体到初始状态
        
        子类必须实现此方法来定义重置逻辑
        """
        pass
    
    def is_off_screen(self, screen_height: int) -> bool:
        """
        检查实体是否离开屏幕
        
        Args:
            screen_height: 屏幕高度
            
        Returns:
            bool: 如果实体离开屏幕返回 True
        """
        return self.rect.top > screen_height
