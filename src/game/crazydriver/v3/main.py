import logging

from resources import ResourceManager

if __name__ == '__main__':
    # 配置日志
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d:  %(message)s',
        datefmt='%H:%M:%S'
    )
    ResourceManager().load_image('Player.png')
