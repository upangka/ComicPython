class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        生成不含重复数字数组的全排列。

        使用回溯 + 标记数组，深度优先遍历决策树。

        Args:
            nums: 不含重复数字的整数列表

        Returns:
            所有可能排列的列表，每个排列是一个 list[int]

        时间复杂度：O(n × n!)，共 n! 个叶子，每个叶子复制列表 O(n)
        空间复杂度：O(n)，递归栈 + used 数组 + path 临时列表
        """
        nums_len: int = len(nums)
        res: list[list[int]] = []
        used: list[bool] = [False] * nums_len  # 标记数组：used[i] 表示 nums[i] 是否已被选
        path: list[int] = []  # 当前正在构建的排列

        def dfs() -> None:
            if len(path) == nums_len:
                res.append(path[:])
                return
            for i in range(nums_len):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])

                # 继续深度遍历
                dfs()

                # 撤销选择（回溯的精髓：恢复状态）
                used[i] = False
                path.pop()

        dfs()
        return res
