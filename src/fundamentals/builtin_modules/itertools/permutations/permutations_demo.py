def permutations_basic():
    """
    演示全排列：从 n 个元素中取出 n 个元素进行排列
    
    数学公式: P(n,n) = n!
    示例: P(3,3) = 3! = 6 种排列
    """
    from itertools import permutations
    assert list(permutations([1, 2, 3])) == [
        (1, 2, 3),
        (1, 3, 2),
        (2, 1, 3),
        (2, 3, 1),
        (3, 1, 2),
        (3, 2, 1)
    ]


def permutations_with_r():
    """
    演示指定长度的排列：从 n 个元素中取出 r 个元素进行排列
    
    数学公式: P(n,r) = n! / (n-r)!
    示例: P(3,2) = 3! / (3-2)! = 6 / 1 = 6 种排列
    
    注意: permutations 返回的是迭代器，需要使用 list() 转换为列表
          每个排列结果是元组 (tuple)，不是列表 (list)
    """
    from itertools import permutations

    # 从3个元素中取2个排列
    result = list(permutations([1, 2, 3], 2))
    assert result == [
        (1, 2), (1, 3),
        (2, 1), (2, 3),
        (3, 1), (3, 2)
    ]
    assert len(result) == 6  # P(3,2) = 6


if __name__ == '__main__':
    permutations_basic()
    permutations_with_r()
