

import itertools

strs = list('ABCDEFG')
it = iter(strs)
# 消耗迭代器前两个元素
print(list(itertools.islice(it,2)))
print(list(it))