class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """计算从左上角到右下角的不同路径数量
        机器人位于一个 m x n 网格的左上角，每次只能向下或向右移动一步，
        计算到达右下角的不同路径总数。
        Args:
            m (int): 网格的行数
            n (int): 网格的列数

        Returns:
            int: 从左上角到右下角的不同路径数量
        """
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
