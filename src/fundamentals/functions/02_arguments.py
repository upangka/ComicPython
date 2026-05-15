def func(a, b, c):
    print(f"{a=} {b=} {c=}")


func(1, c=3, b=2)
# 位置参数
func(1, 2, 3)

# 关键字参数
func(c=3, b=2, a=1)

# 位置参数必须在关键字参数之前
# func(c=3, b=2, 1)  # ❌️SyntaxError: positional argument follows keyword argument
func(1, c=3, b=2)

# 可迭代对象拆包
# values = ("深圳", "图书馆","北馆")
# func(*values)

values = {
    "a": "深圳",
    "b": "图书馆",
    "c": "北馆"
}
func(*values)
func(**values)