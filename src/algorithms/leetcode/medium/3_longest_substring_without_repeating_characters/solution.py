class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        记录当前窗口内的字符。当右指针新加入的字符已经在窗口中时，窗口违法——需要收缩左指针，一直缩到重复字符被移除为止。
        元素集合不需要维护有序性，因为left在s上就是有序的

        Examples:
            >>> Solution().lengthOfLongestSubstring("abcabcbb")
            3
            >>> Solution().lengthOfLongestSubstring("bbbbb")
            1
            >>> Solution().lengthOfLongestSubstring("pwwkew")
            3
        """
        seen = set()
        left = 0
        result = 0
        for right,char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char)
            result = max(result, right - left + 1)
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)