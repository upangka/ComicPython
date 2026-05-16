"""
类型安全的装饰器：使用 Concatenate 注入参数

本模块展示了如何使用 Concatenate 和 ParamSpec 创建类型安全的装饰器。
通过 Concatenate[Request, P]，装饰器可以自动向被装饰函数注入 Request
对象作为第一个参数，同时保持完整的类型信息。调用者无需显式传递
request 参数，类型检查器能正确验证代码。
"""
import functools
from collections.abc import Callable
from typing import Concatenate


class Request:
    """模拟请求对象"""

    def __init__(self, *, ip: str):
        self.ip = ip


_current_request: Request | None = None


def set_current_request(request: Request):
    """设置当前请求对象"""
    global _current_request
    _current_request = request


def get_current_request() -> Request:
    """获取当前请求对象"""
    assert _current_request is not None, "当前请求对象未设置"
    return _current_request


def with_request[**P, R](func: Callable[Concatenate[Request, P], R]) -> Callable[P, R]:
    """装饰器：自动注入 Request 对象作为第一个参数
    
    使用 Concatenate 将 Request 类型添加到函数签名的开头，
    使被装饰函数无需显式接收 request 参数，装饰器会自动注入。
    """""

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs):
        """包装函数"""
        request = get_current_request()
        return func(request, *args, **kwargs)

    return wrapper


@with_request
def get_user(request: Request, user_id: int):
    """模拟获取用户信息"""
    return {
        "user_id": user_id,
        "ip": request.ip,
    }


if __name__ == '__main__':
    set_current_request(Request(ip="2.26.97.21"))
    r = get_user(user_id=3)
    print(r)

"""输出
{'user_id': 3, 'ip': '2.26.97.21'}
"""
