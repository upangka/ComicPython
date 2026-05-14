import itertools
from collections import deque
from collections.abc import Iterable

def moving_average(iterable: Iterable, n: int = 3):
    """滚动求平局值"""
    it = iter(iterable)
    d = deque(itertools.islice(it, n - 1))
    d.appendleft(0)
    s = sum(d)
    for el in it:
        s += el - d.popleft()
        d.append(el)
        yield s / n


gen = moving_average([40, 30, 50, 46, 39, 44], 3)
try:
    while True:
        print(next(gen), end=" ")
except StopIteration:
    print("Done")

"""输出
40.0 42.0 45.0 43.0 Done
"""
