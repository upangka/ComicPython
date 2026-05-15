"""
演示Python中仅关键字形参（Keyword-Only Parameters）的使用方法
"""


def kwonly1(*args, c):
    print(f"{args=} {c=}")


kwonly1(1, 2, c=3)
kwonly1(c=3)
"""输出
args=(1, 2) c=3
args=() c=3
"""


def kwonly2(a, b=42, *, c=3):
    print(f"{a=} {b=} {c=}")

kwonly2(1, 2, c=3)
kwonly2(1, c=3)
"""输出
a=1 b=2 c=3
a=1 b=42 c=3
"""
