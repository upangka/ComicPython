import time
from typing import Callable


def timer(func: Callable):
    """一个简单的计时装饰器"""

    def wrapper():
        start = time.perf_counter()
        result = func()
        print(f"[timer] {func.__name__} 耗时：{time.perf_counter() - start:.2} 秒")
        return result

    return wrapper


@timer
def greet():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"现在的时间是：{current_time}\n我在深圳图书馆北馆学习。")
    time.sleep(3)


greet()

"""输出
现在的时间是：2026-05-15 22:27:22
我在深圳图书馆北馆学习。
[timer] greet 耗时：3.0 秒
"""

open("zen_of_python.txt", mode="w",encoding="utf-8")