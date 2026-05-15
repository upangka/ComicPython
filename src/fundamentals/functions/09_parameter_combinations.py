"""
演示Python中形参的组合使用方法
"""


def func(*, kw):
    pass


func(kw=1)


def func_2(a=None):
    """a 是可选的——调用时可以不传"""
    if a is not None:
        """do something"""
        ...


def func_3(a):
    """a 是必传的——调用时必须提供"""
    pass


func_2()
func_3(2)


def all_params(a, /, b, c=28, *args, d=256, e, **kwargs):
    print(f"{a=} {b=} {c=} {args=} {d=} {e=} {kwargs=}")


all_params(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, e=11, f=12, g=13)
"""输出
a=1 b=2 c=3 args=(4, 5, 6, 7, 8, 9, 10) d=256 e=11 kwargs={'f': 12, 'g': 13}
"""
