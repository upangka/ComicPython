"""
装饰器不使用 wraps 的问题

本模块展示了在装饰器中不使用 functools.wraps 时出现的问题。
被装饰函数会丢失原始的 __name__、__doc__、__annotations__ 等元数据，
导致调试困难、文档生成错误以及 introspection 功能失效。
"""



import time
from collections.abc import Callable

def timer[**P, R](func: Callable[P, R]) -> Callable[P, R]:

    def wrapper(*args: P.args, **kwargs: P.kwargs):
        """我是wrapper"""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"[timer] {func.__name__} 耗时：{time.perf_counter() - start:.2} 秒")
        return result

    return wrapper

@timer
def greet(name, msg="我在深圳图书馆北馆学习"):
    """HI learning 深圳"""
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"现在的时间是：{current_time}\n Hi {name} \n{msg}")
    time.sleep(3)

# 验证元数据丢失
print(f"__name__:       {greet.__name__}")
print(f"__doc__:        {greet.__doc__}")
print(f"__annotations__:{greet.__annotations__}")
print(f"__wrapped__ 存在? {hasattr(greet, '__wrapped__')}")

import inspect
print(f"signature:      {inspect.signature(greet)}")

"""输出
__name__:       wrapper
__doc__:        我是wrapper
__annotations__:{'args': P.args, 'kwargs': P.kwargs}
__wrapped__ 存在? False
signature:      (*args: P.args, **kwargs: P.kwargs)
"""