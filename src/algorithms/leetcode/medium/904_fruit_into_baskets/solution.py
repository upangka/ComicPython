from collections import Counter


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        """计算最多能收集的水果数量（最多只能收集两种水果）。

        Examples:
            >>> Solution().totalFruit([1, 2, 1])
            3
            >>> Solution().totalFruit([0, 1, 2, 2])
            3
            >>> Solution().totalFruit([1, 2, 3, 2, 2])
            4
        """
        basket = Counter()
        left = 0
        result = 0

        for right, fruit in enumerate(fruits):
            basket[fruit] += 1
            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                left += 1
            result = max(result, right - left + 1)
        return result


if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
