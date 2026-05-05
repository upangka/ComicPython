"""碰撞检测管理器"""
import pygame


class CollisionManager:
    """
    碰撞检测管理器
    
    负责处理游戏中所有的碰撞检测逻辑
    """
    
    @staticmethod
    def check_player_enemy_collision(
        player: pygame.sprite.Sprite,
        enemies: pygame.sprite.Group
    ) -> bool:
        """
        检测玩家与敌人的碰撞
        
        Args:
            player: 玩家精灵对象
            enemies: 敌人精灵组
            
        Returns:
            bool: 如果发生碰撞返回 True，否则返回 False
        """
        return pygame.sprite.spritecollideany(player, enemies) is not None
    
    @staticmethod
    def check_multiple_collisions(
        sprite: pygame.sprite.Sprite,
        group: pygame.sprite.Group
    ) -> list:
        """
        检测一个精灵与精灵组中所有碰撞的对象
        
        Args:
            sprite: 要检测的精灵
            group: 精灵组
            
        Returns:
            list: 碰撞到的精灵列表
        """
        return pygame.sprite.spritecollide(sprite, group, False)
