class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        # 逐行滚动更新，用 _ 表示不关心具体行号
        for _ in range(1, m):
            for j in range(1, n):
                # dp[j] 还是上一行的值（上方）
                # dp[j-1] 是本行刚更新的值（左方）
                dp[j] += dp[j - 1]

        return dp[-1]
