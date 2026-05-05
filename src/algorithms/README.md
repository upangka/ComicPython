
Python算法与LeetCode刷题

> Skill技能

## DeepSeek使用

能够生成Mermaid 流程图，比如:
```mermaid
graph TD
    subgraph "f(5) 的递归调用树（部分）"
        A[f5] --> B[f4]
        A --> C[f3]
        B --> D[f3]
        B --> E[f2]
        C --> F[f2]
        C --> G[f1]
        D --> H[f2]
        D --> I[f1]
    end
```

## Python风格

符合python语言风格，比如用到内置模块支持

不行： 
```python
class Solution:
    # 记忆化字典，用于存储已计算的子问题结果，避免重复计算
    memo = {}

    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        if n not in self.memo:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]
```
OK: 使用了内置模块支持
```python
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
```
