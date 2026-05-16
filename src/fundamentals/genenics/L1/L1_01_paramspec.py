"""
ParamSpec：捕获函数参数签名

本模块介绍了 ParamSpec 的使用，用于捕获和保留函数的完整参数签名信息。
ParamSpec 可以捕获位置参数、关键字参数以及它们的类型注解，在装饰器和
高阶函数中保持类型安全，确保参数传递的正确性。
"""
import time
from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def add_timer(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"[timer] {func.__name__} 耗时：{time.perf_counter() - start:.2} 秒")
        return result

    return wrapper

"""新语法
def add_timer[**P,R](func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"[timer] {func.__name__} 耗时：{time.perf_counter() - start:.2} 秒")
        return result

    return wrapper
"""

@add_timer
def learning_python(name, /, when, where, *, note):
    time.sleep(3)
    print(f"{name}在{when}于{where}学习Python，备注：{note}")


if __name__ == '__main__':
    learning_python("Pkmer", where="深圳图书馆北馆", when="2026-05-16", note="Happy Coding :)")

"""输出
Pkmer在2026-05-16于深圳图书馆北馆学习Python，备注：Happy Coding :)
[timer] learning_python 耗时：3.0 秒
"""