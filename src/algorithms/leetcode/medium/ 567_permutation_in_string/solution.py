class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """判断 s2 是否包含 s1 的排列
        换句话说：s2 中是否存在一个长度等于 s1 的窗口，使得窗口内各字符的频数恰好等于 s1 中各字符的频数。

        Args:
            s1: 目标字符串
            s2: 搜索字符串

        Returns:
            bool: 如果 s2 包含 s1 的排列则返回 True，否则返回 False

        Examples:
            >>> Solution().checkInclusion("ab", "eidbaooo")
            True
            >>> Solution().checkInclusion("ab", "eidboaoo")
            False
        """
        from collections import Counter
        window_size = len(s1)
        target_freq = Counter(s1)
        window_freq = Counter(s2[:window_size])

        # 滑动窗口的判断应该在滑动完成之后进行，而不是之前。 标准顺序是：滑动 → 判断 → 下一轮。
        if window_freq == target_freq:
            return True

        for i, right_char in enumerate(s2[window_size:], start=window_size):
            left_char = s2[i - window_size]
            window_freq[left_char] -= 1
            window_freq[right_char] += 1
            if window_freq[left_char] == 0:
                del window_freq[left_char]
            if window_freq == target_freq:
                return True

        return False


if __name__ == '__main__':
   import doctest
   doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
