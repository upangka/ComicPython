from collections.abc import Sequence
from typing import Iterator, Iterable


class OddEven:
    """可迭代对象（只负责创建迭代器）"""
    def __init__(self, data: Sequence):
        self._data = data
        self.index = list(range(0, len(data), 2)) + list(range(1, len(data), 2))

    def __iter__(self):
        """返回一个新的迭代器实例"""
        return OddEvenIterator(self._data)

class OddEvenIterator:
    """迭代器（负责实际遍历）- 高效版本"""
    def __init__(self, data: Sequence):
        self._data = data
        self.current_index = 0
        self._even_finished = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self._data):
            if not self._even_finished:
                self._even_finished = True
                self.current_index = 1
            else:
                raise StopIteration
        result = self._data[self.current_index]
        # 更新索引
        self.current_index += 2
        return result

odd_even = OddEven("ThIsIsCoOl")
print("-".join([c for c in odd_even]))
print("-".join([c for c in odd_even]))