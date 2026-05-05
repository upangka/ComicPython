class Solution:
    # 记忆化字典，用于存储已计算的子问题结果，避免重复计算
    memo = {}

    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        if n not in self.memo:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]


if __name__ == '__main__':
    print(Solution().climbStairs(44))
