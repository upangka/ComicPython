class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        """
        滑动窗口： 遍历 → 入窗(0的计数+1) → while 0太多 → 出窗(0的计数-1) → 更新答案
        """
        left = 0
        result = 0
        # 记录当前0的个数
        curr = 0
        for right,num in enumerate(nums):
            if not num: curr += 1
            while curr > k:
                if not nums[left]: curr -= 1
                left += 1
            result = max(result,right - left + 1)
        return result
