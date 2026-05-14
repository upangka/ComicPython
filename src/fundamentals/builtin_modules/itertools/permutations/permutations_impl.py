"""
实现permutations
"""

from collections.abc import Iterable, Iterator

def permutations_py[T](iterable: Iterable[T], r: int | None = None) -> Iterator[tuple[T, ...]]:
    """
    生成 iterable 中元素的所有 r 长度排列。

    若 r 未指定，默认为 len(iterable)，生成全排列。
    排列按 iterable 原始顺序的字典序生成（输入已排序时结果也排序）。

    Args:
        iterable: 可迭代对象，元素需可哈希（用于去重检测）
        r: 排列长度，必须 <= len(iterable)（若 iterable 有长度）

    Yields:
        tuple[T, ...]: 每个排列的元组

    算法复杂度：时间 O(n!/(n-r)!)，空间 O(n)
    """
    # 第一步：将输入物化为元组（必须的，因需要索引和多次遍历）
    pool: tuple[T,...] = tuple(iterable)
    n: int = len(pool)
    r = n if r is None else r

    if r > n:
        return # 回空迭代器，不会抛异常

    # 核心：初始化索引数组，这是回溯算法的"状态"
    indices: list[int] = list(range(n))
    cycles: list[int] = list(range(n, n - r, -1))  # 控制回溯的"剩余可选数"

    # 第一个排列：取前 r 个元素
    yield tuple(pool[i] for i in indices[:r])

    # 主循环，生成后续排列
    while True:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i]==0:
                # 当前位已穷尽所有选择，重置并左移
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                # 交换
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                # 📌重点：注意这里要break退出for循环，继续从最右边开始找下一个位置
                break
        else:   # 读作 "no break"
             return

if __name__ == '__main__':
    from pprint import pprint
    pprint(list(permutations_py(list('ABCD'),3)))