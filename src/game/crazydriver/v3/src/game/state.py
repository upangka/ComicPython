from __future__ import annotations

import logging
from abc import ABC, abstractmethod

from pygame.locals import *

logger = logging.getLogger(__name__)


class BaseState(ABC):
    """游戏状态抽象类
    定义了游戏状态的接口，子类必须实现 update 和 render 方法。
    """

    def __init__(self, context: GameStateManager):
        self._context = context

    @abstractmethod
    def handle_keypress(self, keys):
        """处理按键"""
        ...

    @abstractmethod
    def _update_sprites(self):
        """更新游戏状态"""
        ...

    @abstractmethod
    def _change_state(self):
        """切换游戏状态"""
        ...


class RunningState(BaseState):
    """运行状态"""

    def __init__(self, context: GameStateManager):
        super().__init__(context)

    def handle_keypress(self, keys):
        self._update_sprites()
        if keys[K_SPACE]:
            self._change_state()

    def _update_sprites(self):
        self._context.engine.update_sprites()

    def _change_state(self):
        self._context.current_state = GameState.PAUSED


from enum import Enum


class GameState(Enum):
    """游戏状态枚举类"""
    RUNNING = 1
    PAUSED = 2
    GAME_OVER = 3


class GameStateManager:
    """游戏状态管理器
    
    负责管理游戏的不同状态（运行、暂停、游戏结束等），
    并在状态之间进行切换。
    """

    def __init__(self, engine):
        """初始化游戏状态管理器
        Args:
            engine: GameEngine 实例，用于访问游戏引擎的核心功能
        """
        self.available_states = {
            GameState.RUNNING: RunningState(self),
        }
        self._current_state = GameState.RUNNING
        self.engine = engine

    def handle_keypress(self, keys):
        self.available_states[self.current_state].handle_keypress(keys)

    @property
    def current_state(self):
        return self._current_state

    @current_state.setter
    def current_state(self, state: GameState):
        logger.debug(f"当前状态: {self.current_state.name}")
        if state not in self.available_states:
            logger.error(f"Invalid state: {state}")
            raise ValueError(f"Invalid state: {state}")

        self._current_state = state
        logger.info(f"状态更新为: {state.name}")

    def __str__(self):
        return f"当前状态: {self.current_state.name}"

    __repr__ = __str__
