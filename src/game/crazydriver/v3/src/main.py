import logging

from game import GameEngine
from settings import GameConfig


def main():
    cfg = GameConfig.from_bg_image('Road.png')
    engine = GameEngine(cfg)


if __name__ == '__main__':
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d:  %(message)s',
        datefmt='%H:%M:%S'
    )
    # main()
    # 查看当前搜索路径
    import sys

    for path in sys.path:
        print(path)