"""游戏配置模块 - 使用 dataclass 和 enum 管理配置"""
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path


class GameState(Enum):
    """游戏状态枚举"""
    RUNNING = "running"
    PAUSED = "paused"
    GAME_OVER = "game_over"


@dataclass(frozen=True)
class GameConfig:
    """游戏配置（不可变）"""
    # 屏幕尺寸
    SCREEN_WIDTH: int = 500
    SCREEN_HEIGHT: int = 800
    
    # 帧率
    FPS: int = 60
    
    # 速度配置
    PLAYER_SPEED: int = 5
    MAX_SPEED: int = 10
    
    # 颜色配置
    COLORS: dict = field(default_factory=lambda: {
        'BLACK': (0, 0, 0),
        'WHITE': (255, 255, 255),
        'RED': (255, 0, 0),
    })
    
    # 字体配置
    FONT_SIZE: int = 40
    
    @property
    def RESOURCES_DIR(self) -> Path:
        """资源根目录"""
        return Path(__file__).parent
    
    @property
    def IMAGES_DIR(self) -> Path:
        """图片目录"""
        return self.RESOURCES_DIR / 'images'
    
    @property
    def FONTS_DIR(self) -> Path:
        """字体目录"""
        return self.RESOURCES_DIR / 'fonts'
    
    @property
    def FONT_PATH(self) -> Path:
        """默认字体路径"""
        return self.FONTS_DIR / '字心坊小呀小布丁.TTF'
