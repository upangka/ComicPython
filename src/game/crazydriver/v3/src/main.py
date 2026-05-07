import logging

from game import GameEngine


def main():
    engine = GameEngine()
    try:
        engine.run()
    except Exception as e:
        logging.error(f'游戏异常退出: {str(e)}')
        raise


if __name__ == '__main__':
    # 配置日志
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d:  %(message)s',
        datefmt='%H:%M:%S'
    )

    main()
    # 查看当前搜索路径
    # import sys
    #
    # for path in sys.path:
    #     print(path)
