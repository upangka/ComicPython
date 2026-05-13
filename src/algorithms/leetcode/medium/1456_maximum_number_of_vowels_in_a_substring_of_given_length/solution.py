class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        入窗 = 该字符是不是元音（1 或 0），出窗 = 该字符是不是元音（1 或 0）
        Examples:
            >>> Solution().maxVowels("abciiidef", 3)
            3
        """
        is_vowels = lambda x: x in "aeiou"
        curr = sum(is_vowels(x) for x in s[:k])
        max_cnt = curr
        for i in range(k, len(s)):
            curr += is_vowels(s[i]) - is_vowels(s[i - k])
            max_cnt = max(max_cnt, curr)
        return max_cnt

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)