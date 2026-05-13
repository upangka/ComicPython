from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """找出 s 中涵盖 t 所有字符的最小子串。

        "窗口包含 t 所有字符" = window 中每个字符的频数 ≥ need 中对应的频数
        使用match来简化target和window对对比

        Examples:
            >>> Solution().minWindow("ADOBECODEBANC", "ABC")
            'BANC'
            >>> Solution().minWindow("a", "a")
            'a'
            >>> Solution().minWindow("a", "aa")
            ''
        """
        # 边界检查
        if not s: return s

        target = Counter(t)
        window = Counter()
        left = 0
        result = s * 2  # 哨兵 初始化一个不可能的答案
        # 当某个字符在 window 中的频数刚好达到 target 中的频数时
        # matched += 1；跌出时 matched -= 1。
        match = 0
        for right, char in enumerate(s):
            window[char] += 1
            if window[char] == target[char]:
                match += 1
            while match == len(target):
                result = s[left:right + 1] if len(result) > (right - left + 1) else result
                left_char = s[left]
                window[left_char] -= 1
                if window[left_char] < target[left_char]:
                    match -= 1
                left += 1
        return result if len(result) <= len(s) else ""


if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
