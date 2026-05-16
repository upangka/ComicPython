"""
装饰器导致的函数签名丢失问题

本模块展示了使用简单装饰器时出现的函数元数据丢失问题。
当函数被装饰后，其 __name__、__doc__ 等属性会被包装函数取代，
导致调试、文档生成和 introspection 出现问题。
"""

import time
from typing import Callable


def timer(func: Callable):
    """一个简单的计时装饰器"""

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"[timer] {func.__name__} 耗时：{time.perf_counter() - start:.2} 秒")
        return result

    return wrapper


@timer
def greet(name: str):
    """Hi 此刻我在深圳图书馆北馆
    Hi Learn Python Programming 3rd Edition
    """
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"现在的时间是：{current_time}\n{name}在深圳图书馆北馆学习。")
    time.sleep(3)


print(f"{greet.__name__ = }")
print(f"{greet.__doc__ = }")
print(f"{greet.__annotations__ = }")
