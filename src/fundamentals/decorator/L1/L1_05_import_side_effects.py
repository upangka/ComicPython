"""
装饰器在导入时执行副作用的问题

本模块展示了装饰器在模块导入阶段就会执行被装饰函数之外的代码，
可能导致意外的副作用。例如：数据库连接、文件操作、网络请求等
不应在导入时执行的操作会被意外触发。
"""

print("模块开始加载")


def register(func):
    print(f"[装饰器] 正在注册: {func.__name__}")
    return func


@register
def my_func():
    pass


print("模块加载完成")
