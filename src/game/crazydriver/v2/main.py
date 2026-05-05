"""疯狂赛车游戏 - 主入口文件

重构版本 v2：使用面向对象设计和设计模式
"""
import sys
from pathlib import Path

# 将当前目录添加到 Python 路径
sys.path.insert(0, str(Path(__file__).parent))

from game.engine import GameEngine


def main():
    """游戏主函数"""
    # 创建游戏引擎实例
    game = GameEngine()
    
    # 运行游戏
    try:
        game.run()
    except Exception as e:
        print(f"游戏运行出错: {e}")
        raise


if __name__ == '__main__':
    main()
