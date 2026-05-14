class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """暴力求解"""
        result = []
        for i in range(len(nums) - k + 1):
            result.append(max(nums[i:i+k]))
        return result
