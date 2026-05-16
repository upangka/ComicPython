"""
L2 装饰器语法：参数化重试装饰器（@语法糖方式）

本模块展示了如何使用 @ 语法糖应用带参数的装饰器。
与手动调用方式相比，使用 @retry_factory(times=3, delay=0.5) 的方式
更加简洁和 Pythonic。装饰器工厂返回的装饰器会自动应用到被装饰函数上。
"""
import time
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def retry_factory(times: int = 2, delay: float = 0.5):
    """装饰器工厂创建一个装饰器
    Args:
        times: 最大重试次数
        delay: 每次重试间隔（秒）
    Returns:
        一个装饰器
    """

    def retry(func):
        """重试装饰器"""
        def wrapper(*args, **kwargs):
            """重试逻辑"""
            for i in range(times):
                try:
                    return func()
                except Exception as e:
                    logger.info(f"第 {i + 1} 次重试失败，错误信息：{e}")
                    if i == times - 1:
                        raise e
                    time.sleep(delay)

        return wrapper

    return retry


@retry_factory(times=3, delay=0.5)
def risk_call():
    """模拟不稳定的操作：70% 概率失败"""
    import random
    if random.random() < 0.7:
        raise ConnectionError("❌️网络不稳定")
    return "✅ 调用成功！"


if __name__ == '__main__':
    """运行多次看效果"""
    for _ in range(2):
        print(risk_call())
        print("─" * 30)
        time.sleep(1)