"""游戏引擎 - 核心游戏逻辑和主循环"""
import sys
import pygame
from config import GameConfig, GameState
from resources import ResourceManager
from entities.player import Player, PlayerInput
from entities.enemy import EnemyFactory
from entities.ui import GameOverUI, PauseUI
from game.state import GameStateManager
from managers.collision_manager import CollisionManager
from managers.score_manager import ScoreManager


class GameEngine:
    """
    游戏引擎类
    
    负责管理游戏的整个生命周期，包括初始化、主循环、渲染等
    """
    
    def __init__(self):
        """初始化游戏引擎"""
        # 初始化 Pygame
        pygame.init()
        
        # 加载配置
        self.config = GameConfig()
        
        # 初始化资源管理器
        self.resource_manager = ResourceManager()
        
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(
            (self.config.SCREEN_WIDTH, self.config.SCREEN_HEIGHT)
        )
        pygame.display.set_caption("疯狂赛车")
        
        # 初始化时钟（控制帧率）
        self.clock = pygame.time.Clock()
        
        # 初始化状态管理器
        self.state_manager = GameStateManager()
        
        # 初始化管理器
        self.collision_manager = CollisionManager()
        self.score_manager = ScoreManager()
        
        # 游戏变量
        self.current_speed = self.config.PLAYER_SPEED
        self.running = True
        
        # 初始化游戏实体
        self._init_entities()
        
        # 初始化 UI 组件
        self._init_ui()
    
    def _init_entities(self):
        """初始化游戏实体（玩家、敌人等）"""
        rm = self.resource_manager
        
        # 加载背景图片
        background_path = self.config.IMAGES_DIR / 'Road.png'
        self.background = rm.load_image(background_path)
        
        # 创建玩家
        player_image_path = self.config.IMAGES_DIR / 'Player.png'
        player_image = rm.load_image(player_image_path)
        self.player = Player(
            player_image,
            self.config.SCREEN_WIDTH,
            self.config.SCREEN_HEIGHT
        )
        
        # 创建敌人组
        self.enemies = pygame.sprite.Group()
        
        # 创建所有精灵组（用于批量绘制）- 必须在 _spawn_enemy 之前创建
        self.all_sprites = pygame.sprite.Group(self.player)
        
        # 生成初始敌人
        self._spawn_enemy()
    
    def _init_ui(self):
        """初始化 UI 组件"""
        self.game_over_ui = GameOverUI(
            self.config.SCREEN_WIDTH,
            self.config.SCREEN_HEIGHT
        )
        self.pause_ui = PauseUI(
            self.config.SCREEN_WIDTH,
            self.config.SCREEN_HEIGHT
        )
    
    def _spawn_enemy(self):
        """生成一个新的敌人"""
        enemy = EnemyFactory.create_random_enemy(
            self.resource_manager,
            self.config.SCREEN_WIDTH
        )
        self.enemies.add(enemy)
        self.all_sprites.add(enemy)
    
    def run(self):
        """
        运行游戏主循环
        
        这是游戏的核心循环，处理事件、更新逻辑、渲染画面
        """
        while self.running:
            # 控制帧率
            delta_time = self.clock.tick(self.config.FPS) / 1000.0
            
            # 处理系统事件
            self._handle_events()
            
            # 获取当前游戏状态
            current_state = self.state_manager.get_current_state()
            
            # 获取按键状态
            keys = pygame.key.get_pressed()
            
            # 处理输入
            current_state.handle_input(keys, self)
            
            # 更新游戏逻辑
            current_state.update(self)
            
            # 渲染画面
            current_state.render(self.screen, self)
            
            # 更新显示
            pygame.display.flip()
        
        # 退出游戏
        self._cleanup()
    
    def _handle_events(self):
        """处理 Pygame 事件队列"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update_entities(self):
        """更新所有游戏实体的状态"""
        # 获取玩家输入
        keys = pygame.key.get_pressed()
        player_input = PlayerInput(
            move_left=(keys[pygame.K_LEFT] or keys[pygame.K_a]),
            move_right=(keys[pygame.K_RIGHT] or keys[pygame.K_d]),
        )
        
        # 更新玩家位置
        self.player.update(player_input, self.current_speed)
        
        # 更新所有敌人
        for enemy in self.enemies:
            enemy.update(self.current_speed)
            
            # 检查敌人是否离开屏幕
            if enemy.is_off_screen(self.config.SCREEN_HEIGHT):
                # 重置敌人位置
                enemy.reset(self.config.SCREEN_WIDTH)
                
                # 增加分数
                self.score_manager.add_score(1)
                
                # 增加难度（提高速度）
                if self.current_speed < self.config.MAX_SPEED:
                    self.current_speed += 1
    
    def check_collision(self) -> bool:
        """
        检测碰撞
        
        Returns:
            bool: 如果发生碰撞返回 True
        """
        return self.collision_manager.check_player_enemy_collision(
            self.player,
            self.enemies
        )
    
    def render_game(self, screen: pygame.Surface):
        """
        渲染游戏场景
        
        Args:
            screen: 目标屏幕表面
        """
        # 绘制背景
        screen.blit(self.background, (0, 0))
        
        # 绘制所有精灵
        self.all_sprites.draw(screen)
        
        # 更新窗口标题显示分数
        pygame.display.set_caption(f'疯狂赛车 得分: {self.score_manager.score}')
    
    def render_game_over(self, screen: pygame.Surface):
        """
        渲染游戏结束画面
        
        Args:
            screen: 目标屏幕表面
        """
        # 填充黑色背景
        screen.fill(self.config.COLORS['BLACK'])
        
        # 渲染游戏结束提示
        self.game_over_ui.render(screen)
    
    def render_pause_overlay(self, screen: pygame.Surface):
        """
        渲染暂停覆盖层
        
        Args:
            screen: 目标屏幕表面
        """
        self.pause_ui.render(screen)
    
    def change_state(self, new_state: GameState):
        """
        改变游戏状态
        
        Args:
            new_state: 新的游戏状态
        """
        self.state_manager.change_state(new_state)
    
    def quit(self):
        """退出游戏"""
        self.running = False
    
    def _cleanup(self):
        """清理资源并退出"""
        pygame.quit()
        sys.exit()
