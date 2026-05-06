import logging
import pygame
from resources import resources

if __name__ == '__main__':
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d:  %(message)s',
        datefmt='%H:%M:%S'
    )
    pygame.init()
    resources.load_image('Player.png')
    resources.load_font('字心坊小呀小布丁.TTF', 25)

