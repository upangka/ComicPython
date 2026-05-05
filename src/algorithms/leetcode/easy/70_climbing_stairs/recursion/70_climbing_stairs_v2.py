from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
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
