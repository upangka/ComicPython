"""
使用 mypy 验证装饰器类型安全

本模块展示了如何通过 mypy 静态类型检查工具验证装饰器的类型安全性。
包含故意制造类型错误的示例，演示 mypy 如何捕获参数类型不匹配、
返回值类型错误等问题，确保装饰器在编译期就能发现潜在 bug。
"""

from collections.abc import Callable
from typing import TypeVar, ParamSpec, Concatenate

P = ParamSpec('P')
R = TypeVar('R')


def with_appid(func: Callable[Concatenate[str, P], R]) -> Callable[P, R]:
    import uuid
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        """提供依赖注入appid"""
        return func(str(uuid.uuid4()), *args, **kwargs)

    return wrapper


def with_appid_no_annotations(func):
    import uuid
    def wrapper(*args, **kwargs):
        """提供依赖注入appid"""
        return func(str(uuid.uuid4()), *args, **kwargs)

    return wrapper


@with_appid
def get_user(appid: str, user_id: int) -> dict[str, int | str]:
    return {
        "user_id": user_id,
        "appid": appid
    }


print(get_user(user_id=3))

import inspect

print(inspect.signature(get_user))  # (*args: P.args, **kwargs: P.kwargs) -> ~R
print(inspect.signature(
    with_appid))  # (func: collections.abc.Callable[typing.Concatenate[str, ~P], ~R]) -> collections.abc.Callable[~P, ~R]
print(inspect.signature(with_appid_no_annotations))  # (func)

# 使用mypy打印签名
reveal_type(get_user)  # Revealed type is "def (user_id: int) -> dict[str, int | str]"
# 这里可以可以很清晰的看到Concatenate的作用
reveal_type(with_appid)  # def [P, R] (func: def (str, *P.args, **P.kwargs) -> R) -> def (*P.args, **P.kwargs) -> R
reveal_type(with_appid_no_annotations)  # def (func: Any) -> Any
