from heapq import (
    heapify,
    heappop,
    heappush)

# 列表转化为堆
heap = [(5, 'write code'), (7, 'release product'), (1, 'write spec'), (3, 'create tests')]
heapify(heap)
print([heappop(heap) for _ in range(len(heap))])
print("*" * 30)

# 堆添加元素
heap = [(5, 'write code'), (7, 'release product'), (1, 'write spec')]
# 要先变成堆✅️
heapify(heap)
heappush(heap, (3, 'create tests'))
print([heappop(heap) for _ in range(len(heap))])
print("*" * 30)

# 从头开始
heap = []
heappush(heap, (5, 'write code'))
heappush(heap, (7, 'release product'))
heappush(heap, (1, 'write spec'))
heappush(heap, (3, 'create tests'))
print([heappop(heap) for _ in range(len(heap))])
