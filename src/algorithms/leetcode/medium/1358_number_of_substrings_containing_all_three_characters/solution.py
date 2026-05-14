from collections import Counter

class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        """
        总数 = 全部子字符串
        最多 2 种 = 缺了至少一种字符的子字符串
        至少包含 3 种 = 总数 - 最多 2 种
        """

        def at_most(k: int) -> int:
            """计算最多k类型窗口下的子串个数
            窗口下的后缀计数
            """
            total = 0
            left = 0
            seen = Counter()

            for right, char in enumerate(s):
                seen[char] += 1
                while len(seen) > k:
                    seen[s[left]] -= 1
                    if seen[s[left]] == 0:
                        del seen[s[left]]
                    left += 1
                total += right - left + 1
            return total

        gauss_sum = lambda n: n * (n + 1) // 2
        return gauss_sum(len(s)) - at_most(2)
