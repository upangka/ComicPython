"""
多个装饰器的应用顺序

本模块展示了如何在一个函数上应用多个装饰器，以及装饰器的执行顺序。
多个装饰器按照从下到上（从内到外）的顺序应用，但执行时按照从上到下
（从外到内）的顺序调用。理解装饰器的堆叠顺序对于正确组合功能至关重要。
"""


def deco_a(func):
    print("[deco_a] 正在包装:", func.__name__)

    def wrapper():
        print("[deco_a] 前置调用")
        func()
        print("[deco_a] 后置调用")

    print("[deco_a] 包装结束")
    return wrapper


def deco_b(func):
    print("[deco_b] 正在包装:", func.__name__)

    def wrapper():
        print("[deco_b] 前置调用")
        func()
        print("[deco_b] 后置调用")

    print("[deco_b] 包装结束")
    return wrapper


@deco_a
@deco_b
def func_one():
    ...


func_one()
print("─" * 30)


@deco_b
@deco_a
def func_two():
    ...


func_two()
"""输出
[deco_b] 正在包装: func_one
[deco_b] 包装结束
[deco_a] 正在包装: wrapper
[deco_a] 包装结束
[deco_a] 前置调用
[deco_b] 前置调用
[deco_b] 后置调用
[deco_a] 后置调用
──────────────────────────────
[deco_a] 正在包装: func_two
[deco_a] 包装结束
[deco_b] 正在包装: wrapper
[deco_b] 包装结束
[deco_b] 前置调用
[deco_a] 前置调用
[deco_a] 后置调用
[deco_b] 后置调用
"""
