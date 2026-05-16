"""
__wrapped__ 属性：访问原始函数

本模块展示了 functools.wraps 如何为包装函数添加 __wrapped__ 属性，
该属性指向被装饰的原始函数。通过 __wrapped__ 可以绕过装饰器直接调用
原始函数，或在运行时检查装饰器链，是调试和高级元编程的重要工具。
"""

import functools
import time
from collections.abc import Callable


def timer[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs):
        """我是wrapper"""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"[timer] {func.__name__} 耗时：{time.perf_counter() - start:.2} 秒")
        return result

    return wrapper


@timer
def greet(name: str, msg: str = "learning 深圳"):
    """HI Pkmer learning 深圳"""
    print(f"Hi {name} {msg}")
    time.sleep(3)

# 直接调用原始函数
greet.__wrapped__("Pkmer")

# 查看包装函数与原始函数的属性差异
print(set(dir(greet)) - set(dir(greet.__wrapped__)))
print(set(dir(greet.__wrapped__)) - set(dir(greet)))
print(len(dir(greet)), len(dir(greet.__wrapped__)))

"""输出
Hi Pkmer learning 深圳
{'__wrapped__'}
set()
39 38
"""




# inspect内部专门处理 __wrapped__ 属性，直接访问最原始的函数
import inspect
print(inspect.signature(greet))

"""输出
(name: str, msg: str = 'learning 深圳')
"""

# inspect内部处理 __wrapped__ 属性
# 获取原始函数的基本原理

unwrap = greet
while True:
    if hasattr(unwrap, '__wrapped__'):
        unwrap = unwrap.__wrapped__
        continue
    break

print(unwrap is greet.__wrapped__) # True
