import logging
import random
import sys

import pygame
from pygame.locals import *

from entities import (
    Player,
    Enemy
)
from entities.player import PlayerInput
from settings import GameConfig
from ui.game_over_tip import GameOverTip
from .score import ScoreManager
from .state import (GameStateManager, GameState)
from .util import check_player_enemy_collision

logger = logging.getLogger(__name__)


class GameEngine:
    """游戏主引擎 - 管理游戏生命周期、事件循环、渲染（门面模式）"""

    def __init__(self):
        self._init_resources()
        self._init_screen()
        self._init_sprite()
        self._st_mgr = GameStateManager(self)
        self.score_mgr = ScoreManager()
        # 帧率控制
        self.clock = pygame.time.Clock()
        self._running = True

    def _init_resources(self):
        """初始化资源"""
        pygame.init()
        self.config = GameConfig.from_bg_image("Road.png")
        self._current_speed = self.config.INITIAL_SPEED
        GameOverTip.config(
            font=self.config.FONT,
            font_size=self.config.FONT_SIZE
        )

    def _init_screen(self):
        """初始化 Pygame"""
        self.screen = pygame.display.set_mode(
            self.config.SCREEN.get_size()
        )
        pygame.display.set_caption(self.config.WINDOW_TITLE)

    def _init_sprite(self):
        """初始化游戏精灵"""
        # 管理所有精灵
        self.all_sprites = pygame.sprite.Group()
        # 单独管理敌人
        self.enemies = pygame.sprite.Group()

        self.player = Player(
            self.config.PLAYER_IMG,
            self.config.SCREEN_WIDTH,
            self.config.SCREEN_HEIGHT
        )
        self.all_sprites.add(self.player)

        for _ in range(3):
            img_name, speed_multiplier, _ = random.choice(self.config.ENEMY_TYPES)
            self.enemy = Enemy(
                img_name,
                self.config.SCREEN_WIDTH,
                self.config.SCREEN_HEIGHT,
                speed_multiplier=speed_multiplier
            )

            self.enemies.add(self.enemy)
            self.all_sprites.add(self.enemy)

    def _process_sys_events(self):
        """处理（消费）游戏系统事件,不然主屏幕会卡住"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._handle_quit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                logger.info("切换状态")
                self._st_mgr.toggle_state()

    def _render(self):
        # 绘制背景
        self.screen.blit(self.config.SCREEN, (0, 0))
        # 绘制所有精灵 比如画一个玩家 self.screen.blit(self.player.image, self.player.rect)
        # group封装了统一处理
        # self.all_sprites.draw(self.screen)

        # 分开绘制
        self.screen.blit(self.player.image, self.player.rect)

        for enemy in self.enemies:
            enemy.active and self.screen.blit(enemy.image, enemy.rect)

        # 得分
        pygame.display.set_caption(f"{self.config.WINDOW_TITLE}  得分: {self.score_mgr.score}")
        pygame.display.update()

    def run(self):
        while self._running:
            try:
                # 添加帧率限制确保游戏运行稳定
                self.clock.tick(self.config.FPS)
                self._process_sys_events()
                self._st_mgr.update_sprites()
                self._render()
            except Exception as e:
                logger.error(f"游戏异常: {str(e)}")

        print("游戏结束")

    def update_sprites(self):
        """更新精灵"""
        keys = pygame.key.get_pressed()
        play_input = PlayerInput(
            move_left=keys[K_LEFT] or keys[K_a],
            move_right=keys[K_RIGHT] or keys[K_d],
            paused=self._st_mgr.current_state == GameState.PAUSED
        )
        self.player.update(
            player_input=play_input,
            speed=self._current_speed
        )

        for enemy in self.enemies:
            if self.enemy.update(speed=self._current_speed):
                logger.debug(f"得分: {self.score_mgr}")
                self.score_mgr.add_score(points=1)
                enemy.reset()
                # 引擎尝试找到不重叠的位置
                enemy.try_non_overlap_position(
                    existing_enemies=self.enemies,
                )

        if check_player_enemy_collision(self.player, self.enemies):
            self._game_over()

    def _wait_with_event_processing(self, seconds: int = 5):
        """等待指定秒数，同时处理系统事件，防止屏幕卡住
        
        Args:
            seconds: 等待的秒数，默认为5秒
        """
        # 根据帧率计算需要等待的帧数
        target_frames = seconds * self.config.FPS
        current_frame = 0

        while current_frame < target_frames:
            self.clock.tick(self.config.FPS)  # 保持帧率稳定
            self._process_sys_events()
            current_frame += 1

    def _render_game_over_screen(self):
        """渲染游戏结束界面，显示多行居中文本"""
        from settings import Color

        # 创建多行文本，计算整体居中位置
        line_height = 50  # 行间距
        lines = [
            GameOverTip(
                text="游戏结束",
                center=(self.config.SCREEN_WIDTH // 2, 0),  # 临时位置，后续调整
                color=Color.RED,
                font_size=40
            ),
            GameOverTip(
                text=f"当前得分: {self.score_mgr.score}",
                center=(self.config.SCREEN_WIDTH // 2, 0),  # 临时位置，后续调整
                color=Color.WHITE
            )
        ]

        # 计算总高度并设置真正的居中位置
        total_height = len(lines) * line_height
        start_y = (self.config.SCREEN_HEIGHT - total_height) // 2 + line_height // 2

        for i, tip in enumerate(lines):
            tip.rect.y = start_y + i * line_height
            tip.render(self.screen)

    def _game_over(self):
        from settings import Color
        self.screen.fill(Color.BLACK)

        # 渲染游戏结束界面
        self._render_game_over_screen()

        pygame.display.flip()

        # 等待5秒，同时处理系统事件，防止屏幕卡住
        self._wait_with_event_processing(5)

        [sprite.kill() for sprite in self.all_sprites]
        self._handle_quit()

    def _handle_quit(self):
        """处理退出游戏"""
        self._running = False
        pygame.quit()
        sys.exit()
