class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """找出数组中满足其和 ≥ target 的长度最小的连续子数组，并返回其长度。

        Examples:
            >>> Solution().minSubArrayLen(7, [2,3,1,2,4,3])
            2
            >>> Solution().minSubArrayLen(4, [1,4,4])
            1
            >>> Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1])
            0
        """
        result = len(nums) + 1  # 哨兵值，代替 float('inf')
        curr = 0
        left = 0

        for right, num in enumerate(nums):
            curr += num
            while curr >= target:
                # 在收缩中更新值
                result = min(result, right - left + 1)
                curr -= nums[left]
                left += 1

        return 0 if result == len(nums) + 1 else result


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
