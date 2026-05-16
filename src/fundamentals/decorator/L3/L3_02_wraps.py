"""
装饰器不使用 wraps 的问题

本模块展示了在装饰器中不使用 functools.wraps 时出现的问题。
被装饰函数会丢失原始的 __name__、__doc__、__annotations__ 等元数据，
导致调试困难、文档生成错误以及 introspection 功能失效。
"""

import functools
import time
from collections.abc import Callable


def timer[**P, R](func: Callable[P, R]) -> Callable[P, R]:

    print(f"{func.__name__} = {func}")
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs):
        """我是wrapper"""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"[timer] {func.__name__} 耗时：{time.perf_counter() - start:.2} 秒")
        return result

    return wrapper


@timer
def greet(name: str, msg: str = "我在深圳图书馆北馆学习"):
    """HI learning 深圳"""
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"现在的时间是：{current_time}\n Hi {name} \n{msg}")
    time.sleep(3)


# 验证元数据丢失
print(f"__name__:       {greet.__name__}")
print(f"__doc__:        {greet.__doc__}")
print(f"__annotations__:{greet.__annotations__}")
print(f"__wrapped__ 存在? {hasattr(greet, '__wrapped__')}")
print(f"后门原始函数 {greet.__wrapped__ =}")
print(f"__dict__ {greet.__dict__ }")


import inspect

print(f"signature:      {inspect.signature(greet)}")

"""输出
greet = <function greet at 0x000002AAD69B1580>
__name__:       greet
__doc__:        HI learning 深圳
__annotations__:{'name': <class 'str'>, 'msg': <class 'str'>}
__wrapped__ 存在? True
后面原始函数 greet.__wrapped__ =<function greet at 0x000002AAD69B1580>
signature:      (name: str, msg: str = '我在深圳图书馆北馆学习')
"""
