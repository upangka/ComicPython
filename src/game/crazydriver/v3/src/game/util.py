"""
游戏工具函数模块

提供游戏中常用的辅助功能，如碰撞检测等。
"""
from entities import Player, Enemy
import pygame

def check_player_enemy_collision(player: Player, enemies) -> bool:
    """检查玩家和敌人是否发生碰撞
    
    Args:
        player: 玩家对象
        enemies: 敌人对象列表
        
    Returns:
        bool: 如果玩家与任何敌人发生碰撞返回True，否则返回False
    """
    return pygame.sprite.spritecollideany(player, enemies) is not None