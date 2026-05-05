"""UI 组件模块 - 游戏界面元素"""
import pygame
from config import GameConfig


class GameOverUI:
    """
    游戏结束 UI 组件
    
    显示游戏结束的提示信息
    """
    
    def __init__(self, screen_width: int, screen_height: int):
        """
        初始化游戏结束 UI
        
        Args:
            screen_width: 屏幕宽度
            screen_height: 屏幕高度
        """
        self.config = GameConfig()
        
        # 加载字体
        self.font = pygame.font.Font(
            str(self.config.FONT_PATH),
            self.config.FONT_SIZE
        )
        
        # 渲染文本
        self.text = self.font.render(
            '游戏结束',
            True,
            self.config.COLORS['RED']
        )
        
        # 计算居中位置
        self.rect = self.text.get_rect(
            center=(screen_width // 2, screen_height // 2)
        )
    
    def render(self, screen: pygame.Surface):
        """
        渲染 UI 到屏幕
        
        Args:
            screen: 目标屏幕表面
        """
        screen.blit(self.text, self.rect)


class ScoreUI:
    """
    分数显示 UI 组件
    
    在屏幕上显示当前分数
    """
    
    def __init__(self, screen_width: int):
        """
        初始化分数 UI
        
        Args:
            screen_width: 屏幕宽度
        """
        self.config = GameConfig()
        self.screen_width = screen_width
        
        # 加载字体
        self.font = pygame.font.Font(
            str(self.config.FONT_PATH),
            30  # 稍小一点的字体
        )
    
    def render(self, screen: pygame.Surface, score: int):
        """
        渲染分数到屏幕
        
        Args:
            screen: 目标屏幕表面
            score: 当前分数
        """
        text = self.font.render(f'得分: {score}', True, self.config.COLORS['BLACK'])
        rect = text.get_rect(topleft=(10, 10))  # 左上角
        screen.blit(text, rect)


class PauseUI:
    """
    暂停提示 UI 组件
    
    显示游戏暂停的提示
    """
    
    def __init__(self, screen_width: int, screen_height: int):
        """
        初始化暂停 UI
        
        Args:
            screen_width: 屏幕宽度
            screen_height: 屏幕高度
        """
        self.config = GameConfig()
        
        # 加载字体
        self.font = pygame.font.Font(
            str(self.config.FONT_PATH),
            self.config.FONT_SIZE
        )
        
        # 渲染文本
        self.text = self.font.render(
            '游戏暂停',
            True,
            self.config.COLORS['BLACK']
        )
        
        # 计算居中位置
        self.rect = self.text.get_rect(
            center=(screen_width // 2, screen_height // 2)
        )
    
    def render(self, screen: pygame.Surface):
        """
        渲染 UI 到屏幕
        
        Args:
            screen: 目标屏幕表面
        """
        screen.blit(self.text, self.rect)
