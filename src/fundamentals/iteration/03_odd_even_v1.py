from collections.abc import Sequence
from typing import Iterator, Iterable

class OddEven:
    """可迭代对象（同时作为迭代器）"""
    def __init__(self, data: Sequence):
        self._data = data
        # 预计算索引：先偶数位置，后奇数位置
        self.index = list(range(0, len(data), 2)) + list(range(1, len(data), 2))

    def __iter__(self):
        """返回自身作为迭代器"""
        return self

    def __next__(self):
        """从预计算的索引中依次获取元素"""
        if self.index:
            return self._data[self.index.pop(0)]
        else:
            raise StopIteration


odd_even = OddEven("ThIsIsCoOl")
print(isinstance(odd_even, Iterator) and isinstance(odd_even, Iterable))
print("-".join([c for c in odd_even]))
# 在获取迭代器，进行获取元素，抛出StopIteration异常
it = iter(odd_even)
next(it) # StopIteration
