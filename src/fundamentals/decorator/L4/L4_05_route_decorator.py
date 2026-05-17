"""
实现路由装饰器：自动解析请求参数

本模块展示了如何实现类似 FastAPI 的路由装饰器，自动从请求对象中
解析并注入参数。通过读取函数签名和类型注解，装饰器能够智能地从
HTTP 请求中提取查询参数、路径参数、请求体等，并转换为正确的类型。
"""
import functools
import inspect
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import ParamSpec, TypeVar, get_type_hints

P = ParamSpec("P")
R = TypeVar("R")

type Handler[R] = Callable[[Request], R]


@dataclass
class Request:
    """HTTP 请求对象"""
    query_params: dict[str, str] = field(default_factory=dict)
    path_params: dict[str, str] = field(default_factory=dict)
    body: dict[str, str] = field(default_factory=dict)


class Router:
    """路由对象"""

    def __init__(self):
        """初始化
        key: (path,method)
        value: Handler
        """
        self._routes: dict[tuple[str, str], Handler] = {}

    @property
    def router(self):
        return self._routes

    def route(self, path: str, method: str = "GET") -> Callable[[Callable[P, R]], Handler[R]]:
        """
        路由装饰器工厂

        关键：返回类型明确标注为 Handler[R]，
        这样 mypy 就知道 get_user 最终类型是 Handler[R] 而不是 Any
        """

        def decorator(func: Callable[P, R]) -> Handler[R]:
            """装饰器"""

            @functools.wraps(func)
            def wrapper(request: Request) -> R:
                sig = inspect.signature(func)
                hints = get_type_hints(func)
                bound = sig.bind_partial()
                for name, annotation in hints.items():
                    if name in request.path_params:
                        bound.arguments[name] = request.path_params[name]
                    elif name in request.query_params:
                        bound.arguments[name] = request.query_params[name]
                    elif name in request.body:
                        bound.arguments[name] = request.body[name]

                return func(*bound.args, **bound.kwargs)

            self._routes[(path, method)] = wrapper
            return wrapper

        return decorator


router = Router()


@router.route("/users/{user_id}")
def get_user(user_id: int, username: str):
    """获取用户信息"""
    print(f"获取用户 {user_id=} 的信息 {username = }")


@router.route(path="/post/{post_id}", method="POST")
def create_post(post_id: int, title: str, content: str):
    """创建帖子"""
    print(f"创建帖子 {post_id=} {title = } {content=}")


# ======================以上代码代码完成注释==================================

from pprint import pprint

pprint(router.router)

# 模拟框架调用

request1 = Request(
    path_params={"user_id": "001"},
    query_params={"username": "Alice"},
    body={},
)

request2 = Request(
    path_params={"post_id": "M03"},
    query_params={},
    body={"title": "Pkmer", "content": "在深圳图书馆学习Learning Python Programming 3rd Edition"},
)

handler1 = router.router[("/users/{user_id}", "GET")]
handler2 = router.router[("/post/{post_id}", "POST")]

for handler, request in zip([handler1, handler2], [request1, request2]):
    handler(request)


"""输出
{('/post/{post_id}', 'POST'): <function create_post at 0x000001E427D30FE0>,
 ('/users/{user_id}', 'GET'): <function get_user at 0x000001E427D30E00>}
获取用户 user_id='001' 的信息 username = 'Alice'
创建帖子 post_id='M03' title = 'Pkmer' content='在深圳图书馆学习Learning Python Programming 3rd Edition'
"""