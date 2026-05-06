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
        self._images: Dict[Path, pygame.Surface] = {}

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
        if image_path not in self._images:
            if not image_path.exists():
                logger.error(f'图片 {img_name} 不存在')
                raise FileNotFoundError(f'图片 {img_name} 不存在')
            self._images[image_path] = pygame.image.load(image_path)
            logger.debug(f'图片缓存中: {img_name}')
        return self._images[image_path]
