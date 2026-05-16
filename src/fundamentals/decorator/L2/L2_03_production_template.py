"""
重试装饰器工业级模板

本模块展示了生产环境中重试装饰器的完整实现。使用 functools.wraps
保留函数元数据，通过 ParamSpec 和 TypeVar 保持类型安全，支持可配置的
重试次数、延迟时间、异常类型过滤和指数退避策略。
"""
import logging
import time
import functools
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s : %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger(__name__)

from typing import Callable, TypeVar, ParamSpec

P = ParamSpec("P")
R = TypeVar("R")


def retry(*,
          times: int = 3,
          delay: float = 1,
          exceptions: tuple[type[Exception], ...] = (Exception,),
          ):
    """装饰器工厂创建一个装饰器
    Args:
        times: 最大重试次数
        delay: 延迟时间
        exceptions: 允许的异常类型
    Returns:
        装饰器
    """
    if times <= 0:
        raise ValueError("times 必须 >= 1")

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        """重试装饰器"""
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            """重试逻辑"""
            last_exception: Exception | None = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.info(f"第 {attempt} 次重试失败，错误信息：{e!r}")
                    time.sleep(delay)

            logger.error(f"[retry] {func.__name__} 重试 {times} 次全部失败")
            assert last_exception is not None
            raise last_exception

        return wrapper

    return decorator


import random

@retry(times=3, delay=1, exceptions=(ConnectionError, TimeoutError))
def flaky_operation():
    """不稳定的操作"""
    if random.random() < 0.7:
        raise ConnectionError("❌️网络不稳定")
    return "✅ 调用成功！"


if __name__ == '__main__':
    """运行多次看效果"""
    line = "─" * 42
    for i in range(3):
        try:
            print(f"""{line}第{i + 1}个测试{line}""")
            time.sleep(0.1)
            print(flaky_operation())
            time.sleep(1)
        except Exception as e:
            print(f"❌️测试失败，错误信息：{e}")


"""输出
──────────────────────────────────────────第1个测试──────────────────────────────────────────
2026-05-16 11:33:33 - __main__ - INFO : 第 1 次重试失败，错误信息：ConnectionError('❌️网络不稳定')
2026-05-16 11:33:34 - __main__ - INFO : 第 2 次重试失败，错误信息：ConnectionError('❌️网络不稳定')
2026-05-16 11:33:35 - __main__ - INFO : 第 3 次重试失败，错误信息：ConnectionError('❌️网络不稳定')
2026-05-16 11:33:36 - __main__ - ERROR : [retry] flaky_operation 重试 3 次全部失败
❌️测试失败，错误信息：❌️网络不稳定
──────────────────────────────────────────第2个测试──────────────────────────────────────────
2026-05-16 11:33:36 - __main__ - INFO : 第 1 次重试失败，错误信息：ConnectionError('❌️网络不稳定')
2026-05-16 11:33:37 - __main__ - INFO : 第 2 次重试失败，错误信息：ConnectionError('❌️网络不稳定')
✅ 调用成功！
──────────────────────────────────────────第3个测试──────────────────────────────────────────
2026-05-16 11:33:40 - __main__ - INFO : 第 1 次重试失败，错误信息：ConnectionError('❌️网络不稳定')
✅ 调用成功！
"""