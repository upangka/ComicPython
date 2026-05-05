from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        """计算爬楼梯的不同方法数

        假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
        每次你可以爬 1 或 2 个台阶。计算有多少种不同的方法可以爬到楼顶。

        使用记忆化递归（自顶向下）的方法实现。
        Args:
            n (int): 楼梯的总阶数

        Returns:
            int: 到达楼顶的不同方法数量
        """

        @cache
        def dfs(n):
            if n <= 2: return n
            return dfs(n - 1) + dfs(n - 2)

        result = dfs(n)
        # 函数调用后查看缓存信息
        print(dfs.cache_info())
        return result


if __name__ == '__main__':
    print(Solution().climbStairs(5))
