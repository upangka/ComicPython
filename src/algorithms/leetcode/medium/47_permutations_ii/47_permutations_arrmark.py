class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        """
        生成包含重复元素数组的所有不重复全排列

        使用深度优先搜索(DFS)和剪枝策略来避免生成重复的排列。
        首先对数组排序，然后在同层递归中跳过相同的元素。

        Args:
            nums: 可能包含重复元素的整数数组

        Returns:
            所有不重复的全排列列表

        Examples:
            >>> Solution().permuteUnique([1, 1, 2])
            [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        """
        nums_len: int = len(nums)
        res: list[list[int]] = []
        used: list[bool] = [False] * nums_len
        path: list[int] = []

        # 排序预处理方便待会剪枝
        nums = sorted(nums)

        def dfs():
            if len(path) == nums_len:
                res.append(path[:])
                return
            for i in range(nums_len):
                if used[i]:
                    continue
                # 剪枝：同层相同元素只取第一个
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                dfs()
                used[i] = False
                path.pop()

        dfs()
        return res;


if __name__ == '__main__':
   import doctest
   doctest.testmod(optionflags=doctest.ELLIPSIS)
