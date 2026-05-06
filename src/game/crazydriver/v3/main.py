import logging

from resources import ResourceManager

if __name__ == '__main__':
    # 配置日志
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'

    )
    ResourceManager().load_image('logo.png')
