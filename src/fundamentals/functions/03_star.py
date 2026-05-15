values = ("深圳", "图书馆", "北馆")

# 贪婪捕获
a, *rest = values
print(f"{a=} {rest=}")

# 展开运算符
print(['我', '爱', *values])
