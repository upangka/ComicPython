"""
装饰器支持被装饰函数有参数的示例

本模块展示了如何创建能够处理带参数函数的装饰器。
通过在包装函数中使用 *args 和 **kwargs，装饰器可以接收并传递
任意数量和类型的参数给被装饰的函数。
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
def greet(name, msg="我在深圳图书馆北馆学习"):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"现在的时间是：{current_time}\n Hi {name} \n{msg}")
    time.sleep(3)


greet("Pkmer")
print("-"*30)
greet("Pkmer", "我正在看《Learn Python Programming 3rd edition》by Fabrizio Romano & Heinrich Kruger")

"""输出
现在的时间是：2026-05-15 22:42:00
 Hi Pkmer 
我在深圳图书馆北馆学习
[timer] greet 耗时：3.0 秒
------------------------------
现在的时间是：2026-05-15 22:42:03
 Hi Pkmer 
我正在看《Learn Python Programming 3rd edition》by Fabrizio Romano & Heinrich Kruger
[timer] greet 耗时：3.0 秒
"""
