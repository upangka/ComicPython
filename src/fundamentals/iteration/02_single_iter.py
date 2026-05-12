
from collections.abc import Iterable,Iterator
# 可迭代对象
msg = "此刻我在深圳的夜里"
print(isinstance(msg, Iterable)) # True
print(isinstance(msg, Iterator)) # False

# 得到迭代器
msg_iter = iter(msg)
print(type(msg_iter), msg_iter)

# 消耗这个迭代器
print(list(msg_iter))
print(list(msg_iter))

# 消耗字符串
print(list(msg))
print(list(msg))