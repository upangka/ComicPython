"""
使用装饰器基于类型注解实现依赖注入

本模块展示了如何通过读取函数的类型注解，自动注入依赖对象。
装饰器分析参数类型，从依赖容器中获取对应实例并注入，
实现类似 FastAPI 的依赖注入机制，减少手动传递依赖的代码。
"""

import functools
import inspect
from collections.abc import Callable
from typing import ParamSpec, TypeVar, Annotated, get_type_hints

P = ParamSpec('P')
R = TypeVar('R')


class DependsOn:
    def __init__(self, func: Callable):
        self.func = func


def my_inject(func):
    """依赖注入装饰器"""
    sig = inspect.signature(func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """包装函数"""
        # 获取函数的参数类型
        parameters = sig.parameters
        # include_extras 对Annotated携带元数据的支持,获取所有参数类型
        hints = get_type_hints(func, include_extras=True)
        # 先绑定用户先传递的参数
        bound = sig.bind_partial(*args, **kwargs)
        # 遍历参数类型，处理DependsOn
        for name, annotation in parameters.items():
            # annotation_type = annotation.annotation
            annotation_type = hints.get(name)
            # 找到Annotated类型注解
            if annotation_type and hasattr(annotation_type, "__metadata__"):
                for metadata in annotation_type.__metadata__:
                    if isinstance(metadata, DependsOn) and name not in bound.arguments:
                        bound.arguments[name] = metadata.func()
        print(bound.arguments)
        return func(*bound.args, **bound.kwargs)

    return wrapper


def get_user() -> dict:
    return {"name": "Pkmer"}


@my_inject
def greet(user: Annotated[dict, DependsOn(get_user)],
          book="Learn Python Programming 3rd Edition",
          *,
          msg: str):
    print(f"{user.get("name")} {msg} {book}")

greet(msg="在深圳，听歌")
