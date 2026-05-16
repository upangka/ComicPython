"""
L2 手工形式：参数化重试装饰器（手动调用方式）

本模块展示了如何创建带有参数的装饰器，并通过手动调用的方式应用装饰器。
通过三层嵌套函数结构，外层函数接收装饰器参数（如重试次数、延迟时间），
中间层接收被装饰函数，内层 wrapper 执行实际的重试逻辑。
使用 factory(times=3, delay=0.5)(func) 的手动方式应用装饰器。
"""
import time
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def retry_factory(times: int = 2, delay: float = 0.5):
    """装饰器工厂创建一个装饰器
    Return:
        装饰器
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


def risk_call():
    """模拟不稳定的操作：70% 概率失败"""
    import random
    if random.random() < 0.7:
        raise ConnectionError("❌️网络不稳定")
    return "✅ 调用成功！"

risk_call = retry_factory(times=3, delay=0.5)(risk_call)

if __name__ == '__main__':
    """运行多次看效果"""
    for _ in range(2):
        print(risk_call())
        print("─" * 30)
        time.sleep(1)

"""输出
INFO:__main__:第 1 次重试失败，错误信息：❌️网络不稳定
✅ 调用成功！
──────────────────────────────
INFO:__main__:第 1 次重试失败，错误信息：❌️网络不稳定
INFO:__main__:第 2 次重试失败，错误信息：❌️网络不稳定
✅ 调用成功！
──────────────────────────────
"""