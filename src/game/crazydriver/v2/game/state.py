"""游戏状态管理 - 使用状态模式管理游戏状态转换"""
from abc import ABC, abstractmethod
import pygame
from config import GameState


class State(ABC):
    """
    状态基类（状态模式）
    
    定义所有游戏状态的通用接口
    """
    
    @abstractmethod
    def handle_input(self, keys: dict, game_engine):
        """
        处理用户输入
        
        Args:
            keys: 按键状态字典
            game_engine: 游戏引擎实例
        """
        pass
    
    @abstractmethod
    def update(self, game_engine):
        """
        更新游戏逻辑
        
        Args:
            game_engine: 游戏引擎实例
        """
        pass
    
    @abstractmethod
    def render(self, screen: pygame.Surface, game_engine):
        """
        渲染游戏画面
        
        Args:
            screen: 屏幕表面
            game_engine: 游戏引擎实例
        """
        pass


class RunningState(State):
    """
    运行状态
    
    游戏正常进行中的状态
    """
    
    def handle_input(self, keys: dict, game_engine):
        """处理暂停键"""
        if keys[pygame.K_SPACE]:
            game_engine.change_state(GameState.PAUSED)
    
    def update(self, game_engine):
        """更新游戏实体和检测碰撞"""
        game_engine.update_entities()
        
        # 检测碰撞
        if game_engine.check_collision():
            game_engine.change_state(GameState.GAME_OVER)
    
    def render(self, screen: pygame.Surface, game_engine):
        """渲染游戏场景"""
        game_engine.render_game(screen)


class PausedState(State):
    """
    暂停状态
    
    游戏暂停时的状态
    """
    
    def handle_input(self, keys: dict, game_engine):
        """处理继续游戏"""
        if keys[pygame.K_SPACE]:
            game_engine.change_state(GameState.RUNNING)
    
    def update(self, game_engine):
        """暂停状态下不更新游戏逻辑"""
        pass
    
    def render(self, screen: pygame.Surface, game_engine):
        """渲染游戏场景并显示暂停提示"""
        game_engine.render_game(screen)
        game_engine.render_pause_overlay(screen)


class GameOverState(State):
    """
    游戏结束状态
    
    玩家碰撞后的结束状态
    """
    
    def __init__(self):
        self.frame_count = 0  # 用于延迟退出
    
    def handle_input(self, keys: dict, game_engine):
        """可以添加重新开始逻辑"""
        # TODO: 可以添加按 R 重新开始的逻辑
        pass
    
    def update(self, game_engine):
        """延迟后退出游戏"""
        self.frame_count += 1
        
        # 5秒后退出（60 FPS * 5 = 300 帧）
        if self.frame_count > 300:
            game_engine.quit()
    
    def render(self, screen: pygame.Surface, game_engine):
        """渲染游戏结束画面"""
        # 只渲染游戏结束画面（黑屏 + 提示文字）
        game_engine.render_game_over(screen)


class GameStateManager:
    """
    游戏状态管理器
    
    管理当前游戏状态并进行状态转换
    """
    
    def __init__(self):
        # 初始化所有状态
        self.states = {
            GameState.RUNNING: RunningState(),
            GameState.PAUSED: PausedState(),
            GameState.GAME_OVER: GameOverState(),
        }
        
        # 初始状态为运行中
        self.current_state_type = GameState.RUNNING
    
    def get_current_state(self) -> State:
        """
        获取当前状态对象
        
        Returns:
            State: 当前状态实例
        """
        return self.states[self.current_state_type]
    
    def change_state(self, new_state: GameState):
        """
        切换到新状态
        
        Args:
            new_state: 新的游戏状态
        """
        if new_state in self.states:
            self.current_state_type = new_state
            
            # 如果切换到游戏结束状态，重置帧计数器
            if new_state == GameState.GAME_OVER:
                self.states[GameState.GAME_OVER].frame_count = 0
    
    def get_current_state_type(self) -> GameState:
        """
        获取当前状态类型
        
        Returns:
            GameState: 当前状态枚举值
        """
        return self.current_state_type
