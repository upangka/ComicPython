from collections import deque


def roundrobin(*iterables):
    iterators = deque([iter(el) for el in iterables])
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                # 循环往左移动一步
                iterators.rotate(-1)
        except StopIteration:
            iterators.popleft()


print(list(roundrobin('ABC', 'D', 'EF')))
"""输出
['A', 'D', 'E', 'B', 'F', 'C']
"""