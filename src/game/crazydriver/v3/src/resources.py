"""资源管理模块

提供 ResourceManager 单例实例，用于统一管理游戏资源。
使用前请确保已调用 pygame.init()。
"""

import logging
from pathlib import Path
from typing import Dict

import pygame

logger = logging.getLogger(__name__)


class ResourceManager:
    """资源管理器

    负责加载和管理游戏资源（图片、字体等），提供缓存机制避免重复加载。

    注意：使用前必须调用 pygame.init() 初始化 pygame。
    """

    def __init__(self):
        self._root = Path(__file__).parent
        self._images_dir = self._root / 'assets' / 'images'
        self._fonts_dir = self._root / 'assets' / 'fonts'

        self._image_cache: Dict[Path, pygame.Surface] = {}
        self._font_cache: Dict[tuple, pygame.font.Font] = {}

        logger.info("ResourceManager 初始化完成")
        logger.debug(f"图片目录: {self._images_dir}")
        logger.debug(f"字体目录: {self._fonts_dir}")

    def load_image(self, img_name: str) -> pygame.Surface:
        """加载图片资源

        从 images 目录加载指定名称的图片，如果已加载则直接返回缓存的表面。

        Args:
            img_name: 图片文件名（包含扩展名），例如 'Player.png'

        Returns:
            pygame.Surface: 加载后的表面对象

        Raises:
            FileNotFoundError: 当指定的图片文件不存在时抛出
            Exception: 当图片加载失败时抛出（例如文件格式损坏）

        Examples:
            >>> manager = ResourceManager()
            >>> player_surface = manager.load_image('Player.png')
        """
        image_path = self._images_dir / img_name

        if image_path not in self._image_cache:
            if not image_path.exists():
                logger.error(f"图片文件不存在: {img_name}, 路径: {image_path}")
                raise FileNotFoundError(f'图片 {img_name} 不存在')

            logger.info(f"加载图片: {img_name}")
            try:
                self._image_cache[image_path] = pygame.image.load(image_path)
                logger.debug(f"图片加载成功: {img_name}, 尺寸: {self._image_cache[image_path].get_size()}")
            except Exception as e:
                logger.error(f"加载图片失败: {img_name}, 错误: {str(e)}")
                raise

        return self._image_cache[image_path]

    def load_font(self, font_name: str, size: int) -> pygame.font.Font:
        """加载字体

        从 fonts 目录加载指定名称和大小的字体，如果已加载则直接返回缓存的字体对象。

        Args:
            font_name: 字体文件名（包含扩展名），例如 '字心坊小呀小布丁.TTF'
            size: 字体大小（像素）

        Returns:
            pygame.font.Font: 加载后的字体对象

        Raises:
            FileNotFoundError: 当指定的字体文件不存在时抛出

        Examples:
            >>> manager = ResourceManager()
            >>> font = manager.load_font('字心坊小呀小布丁.TTF', 24)
            >>> text_surface = font.render("你好", True, (255, 255, 255))
        """
        font_path = self._fonts_dir / font_name
        cache_key = (font_path, size)

        if cache_key not in self._font_cache:
            if not font_path.exists():
                logger.error(f"字体文件不存在: {font_name}, 路径: {font_path}")
                raise FileNotFoundError(f'字体 {font_name} 不存在')

            logger.info(f"加载字体: {font_name}, 大小: {size}")
            try:
                self._font_cache[cache_key] = pygame.font.Font(font_path, size)
                logger.debug(f"字体加载成功: {font_name}")
            except Exception as e:
                logger.error(f"加载字体失败: {font_name}, 错误: {str(e)}")
                raise

        return self._font_cache[cache_key]


resources: ResourceManager = ResourceManager()
"""全局资源管理器单例实例
提供统一的资源加载接口，支持图片和字体的缓存管理。
Example:
    >>> from resources import resources
    >>> font = resources.load_font('字心坊小呀小布丁.TTF', 25)
"""
