"""
使用装饰器基于类型注解实现依赖注入

本模块展示了如何通过读取函数的类型注解，自动注入依赖对象。
装饰器分析参数类型，从依赖容器中获取对应实例并注入，
实现类似 FastAPI 的依赖注入机制，减少手动传递依赖的代码。
"""

from collections.abc import Callable
from typing import ParamSpec, TypeVar, Annotated, get_type_hints

P = ParamSpec('P')
R = TypeVar('R')


class DependsOn:
    def __init__(self, func: Callable):
        self.func = func


def my_inject(func: Callable[P, R]) -> Callable[P, R]:
    """依赖注入装饰器"""
    import inspect
    sig = inspect.signature(func)

    def wrapper(*args, **kwargs) -> R:
        """包装函数"""
        # 获取函数的参数类型
        parameters = sig.parameters
        # include_extras 对Annotated携带元数据的支持
        hints = get_type_hints(func, include_extras=True)
        bound = sig.bind_partial(*args, **kwargs)
        # 遍历参数类型
        for name, annotation in parameters.items():
            # annotation_type = annotation.annotation
            annotation_type = hints.get(name)
            if hasattr(annotation_type, "__metadata__"):
                for metadata in annotation_type.__metadata__:
                    if isinstance(metadata, DependsOn) and name not in bound.arguments:
                        bound.arguments[name] = metadata.func()
        func(*bound.args, **bound.kwargs)

    return wrapper


def get_user() -> dict:
    return {"name": "Pkmer"}


@my_inject
def greet(user: Annotated[dict, DependsOn(get_user)], *, msg: str):
    print(f"{user.get("name")} {msg}")


greet(msg="在深圳，听歌")
