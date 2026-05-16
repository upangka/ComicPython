"""
工业级计时装饰器模板
但签名会丢失
"""
import logging
import time
from time import perf_counter
from typing import Callable

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def timer[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    """装饰器：记录函数耗时，保持原始签名。

        **P: ParamSpec——捕获原始函数的所有参数信息
        R: TypeVar——捕获原始函数的返回值类型
    """

    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            logger.info(f"{func.__name__} 耗时：{perf_counter() - start:.2} 秒")

    # 暂时解决递归的问题
    # wrapper.__wrapper__ = func
    return wrapper


@timer
def greet(name: str, /, msg: str):
    print(f"Hi {name} \n{msg}")
    time.sleep(1)


greet("Pkmer", msg="在深圳图书馆北馆学习")
print("─" * 30)


@timer
def _my_wrapper_test_fib(*, num: int):
    """fib是递归调用
    为方便统计这里用_my_wrapper_test_fib函数进行包装
    """

    def fib(n: int) -> int:
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    r = fib(num)
    print(f"fib({num}) = {r}")


_my_wrapper_test_fib(num=36)

















