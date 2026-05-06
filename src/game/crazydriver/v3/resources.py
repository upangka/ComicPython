import logging
from pathlib import Path
from typing import Dict

import pygame

logger = logging.getLogger(__name__)


class ResourceManager:
    """资源管理"""

    # todo 单例模式

    def __init__(self):
        # 默认为 main.py 所在目录
        self._root = Path(__file__).parent
        self._images_dir = self._root / 'assets' / 'images'
        self._fonts_dir = self._root / 'assets' / 'fonts'

        # 加载图片
        self._image_cache: Dict[Path, pygame.Surface] = {}
        self._font_cache: Dict[Path, pygame.font.Font] = {}


        logger.info(f"ResourceManager 初始化完成")
        logger.debug(f"图片目录: {self._images_dir}")
        logger.debug(f"字体目录: {self._fonts_dir}")

    def load_image(self, img_name: str) -> pygame.Surface:
        """加载图片
        从 images 目录加载指定名称的图片，如果已加载则直接返回缓存的Surface。

        Args:
            img_name: 图片文件名（包含扩展名），例如 'Player.png'

        Returns:
            pygame.Surface: 加载后的表面对象

        Raises:
            FileNotFoundError: 当指定的图片文件不存在时抛出

        Examples:
            >>> manager = ResourceManager()
            >>> player_surface = manager.load_image('Player.png')
        """
        image_path = self._images_dir / img_name
        if image_path not in self._image_cache:
            if not image_path.exists():
                logger.error(f'图片 {img_name} 不存在')
                raise FileNotFoundError(f'图片 {img_name} 不存在')
            self._image_cache[image_path] = pygame.image.load(image_path)
            logger.debug(f'图片缓存中: {img_name}')
        return self._image_cache[image_path]


    def load_font(self, font_name: str, size: int) -> pygame.font.Font:
        """加载字体
        从 fonts 目录加载指定名称和大小的字体，如果已加载则直接返回缓存的字体对象。

        Args:
            font_name: 字体文件名（不包含扩展名），例如 'arial.ttf'
            size: 字体大小

        Returns:
            pygame.font.Font: 加载后的字体对象

        Raises:
            FileNotFoundError: 当指定的字体文件不存在时抛出

        Examples:
            >>> manager = ResourceManager()
            >>> font = manager.load_font('字心坊小呀小布丁.TTF', 25)
        """
        font_path = self._fonts_dir / font_name
        if font_path not in self._font_cache:
            if not font_path.exists():
                logger.error(f'字体 {font_name} 不存在')
                raise FileNotFoundError(f'字体 {font_name} 不存在')
            self._font_cache[font_path] = pygame.font.Font(font_path, size)
            logger.debug(f'字体缓存中: {font_name}')
        return self._font_cache[font_path]
