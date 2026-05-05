"""敌人类模块 - 使用工厂模式创建不同类型的敌人"""
import random
from enum import Enum
import pygame
from .base import BaseEntity


class EnemyType(Enum):
    """敌人类型枚举"""
    BASIC = "basic"      # 普通敌人
    FAST = "fast"        # 快速敌人（未来扩展）
    HEAVY = "heavy"      # 重型敌人（未来扩展）


class Enemy(BaseEntity):
    """
    敌人类
    
    代表赛道上的障碍物，从上往下移动
    """
    
    def __init__(self, image: pygame.Surface, position: tuple, enemy_type: EnemyType = EnemyType.BASIC):
        """
        初始化敌人
        
        Args:
            image: 敌人图像
            position: 初始位置 (x, y)
            enemy_type: 敌人类型
        """
        super().__init__(image, position)
        self.enemy_type = enemy_type
    
    def update(self, speed: int):
        """
        更新敌人位置（向下移动）
        
        Args:
            speed: 移动速度
        """
        self.rect.move_ip(0, speed)
    
    def reset(self, screen_width: int):
        """
        重置敌人到顶部随机位置
        
        Args:
            screen_width: 屏幕宽度
        """
        # 随机生成 x 坐标，确保敌人完全在屏幕内
        min_x = self.image.get_width() // 2
        max_x = screen_width - self.image.get_width() // 2
        x = random.randint(min_x, max_x)
        
        self.rect.center = (x, 0)


class EnemyFactory:
    """
    敌人对象工厂（工厂模式）
    
    负责创建不同类型的敌人对象
    """
    
    # 敌人类型对应的图片文件名
    ENEMY_IMAGES = {
        EnemyType.BASIC: 'Enemy.png',
        EnemyType.FAST: 'Enemy2.png',
        EnemyType.HEAVY: 'Enemy3.png',
    }
    
    @staticmethod
    def create_enemy(
        enemy_type: EnemyType,
        resource_manager,
        screen_width: int
    ) -> Enemy:
        """
        创建敌人对象
        
        Args:
            enemy_type: 敌人类型
            resource_manager: 资源管理器实例
            screen_width: 屏幕宽度
            
        Returns:
            Enemy: 创建的敌人对象
        """
        from resources import ResourceManager
        
        # 获取资源管理器单例
        rm = resource_manager if resource_manager else ResourceManager()
        
        # 根据类型加载对应的图片
        image_name = EnemyFactory.ENEMY_IMAGES[enemy_type]
        image_path = rm.IMAGES_DIR / image_name
        image = rm.load_image(image_path)
        
        # 随机生成初始位置
        min_x = image.get_width() // 2
        max_x = screen_width - image.get_width() // 2
        x = random.randint(min_x, max_x)
        position = (x, 0)
        
        return Enemy(image, position, enemy_type)
    
    @staticmethod
    def create_random_enemy(resource_manager, screen_width: int) -> Enemy:
        """
        创建随机类型的敌人
        
        Args:
            resource_manager: 资源管理器实例
            screen_width: 屏幕宽度
            
        Returns:
            Enemy: 创建的敌人对象
        """
        # 目前只创建基本类型，后续可以扩展随机选择逻辑
        return EnemyFactory.create_enemy(EnemyType.BASIC, resource_manager, screen_width)
