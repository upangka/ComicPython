class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        使用交换法生成全排列（原地交换，不额外使用标记数组）。

        核心思想：位置 i 依次和后面的每个元素交换，然后递归处理 i+1 及之后。
        这和 itertools.permutations 的算法本质相同。

        时间复杂度：O(n × n!)
        空间复杂度：O(n) 递归栈（不计算结果存储）
        """
        results = []
        nums_len = len(nums)
        def dfs(first: int) -> None:
            """
            处理从 first 位置开始的子排列。

            first 之前的位已固定，first 及之后是待选区。
            每次选择待选区中的一个元素交换到 first 位置，然后递归处理 first+1。

            Args:
                first 开始的位置索引
            """
            if first == nums_len:
                results.append(nums[:])
                return
            for i in range(first,nums_len):
                # 将 nums[i] 交换到 first 位置（选中它）
                nums[first], nums[i] = nums[i], nums[first]
                # 递归处理剩余位置
                dfs(first + 1)
                # 撤销交换（恢复原状）
                nums[first], nums[i] = nums[i], nums[first]

        dfs(0) # 从第一个位置开始处理
        return  results

if __name__ == '__main__':
    from pprint import pprint
    pprint(Solution().permute(list('ABC')))

"""输出
[['A', 'B', 'C'],
 ['A', 'C', 'B'],
 ['B', 'A', 'C'],
 ['B', 'C', 'A'],
 ['C', 'B', 'A'],
 ['C', 'A', 'B']]
"""