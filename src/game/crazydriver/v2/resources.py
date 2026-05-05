"""资源管理器 - 单例模式管理游戏资源加载和缓存"""
import pygame
from pathlib import Path
from functools import lru_cache
from typing import Dict, Tuple


class ResourceManager:
    """
    资源管理器（单例模式）
    负责加载和缓存图片、字体等资源，避免重复加载
    """
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        # 初始化路径属性
        self._base_dir = Path(__file__).parent
        self._images_dir = self._base_dir / 'images'
        self._fonts_dir = self._base_dir / 'fonts'
        
        self._images: Dict[Path, pygame.Surface] = {}
        self._fonts: Dict[Tuple[Path, int], pygame.font.Font] = {}
        self._initialized = True
    
    @property
    def IMAGES_DIR(self) -> Path:
        """图片目录"""
        return self._images_dir
    
    @property
    def FONTS_DIR(self) -> Path:
        """字体目录"""
        return self._fonts_dir
    
    @lru_cache(maxsize=128)
    def load_image(self, path: Path) -> pygame.Surface:
        """
        加载图片（带缓存）
        
        Args:
            path: 图片文件路径
            
        Returns:
            pygame.Surface: 加载的图片表面
        """
        if path not in self._images:
            if not path.exists():
                raise FileNotFoundError(f"图片文件不存在: {path}")
            
            # convert_alpha() 保持透明度并优化性能
            self._images[path] = pygame.image.load(str(path)).convert_alpha()
        
        return self._images[path]
    
    def load_font(self, path: Path, size: int) -> pygame.font.Font:
        """
        加载字体（带缓存）
        
        Args:
            path: 字体文件路径
            size: 字体大小
            
        Returns:
            pygame.font.Font: 加载的字体对象
        """
        key = (path, size)
        
        if key not in self._fonts:
            if not path.exists():
                raise FileNotFoundError(f"字体文件不存在: {path}")
            
            self._fonts[key] = pygame.font.Font(str(path), size)
        
        return self._fonts[key]
    
    def clear_cache(self):
        """清除所有缓存的资源"""
        self._images.clear()
        self._fonts.clear()
        self.load_image.cache_clear()
