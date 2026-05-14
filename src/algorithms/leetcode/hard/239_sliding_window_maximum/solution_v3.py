from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        维护一个单调递减队列，存索引。队首永远是当前窗口最大值。
        只保留有竞争力的元素
        """
        # 窗口存储的是当前窗口内元素的索引
        window = deque()
        result = []
        # 固定窗口不用维护left
        for right, val in enumerate(nums):
            # 维护单调性，队列从大到小
            while window and nums[window[-1]] < val:
                window.pop()
            window.append(right)

            left = right - k + 1
            # 窗口形成
            if left >= 0:
                # 维护窗口,清除不在窗口的元素
                while window and window[0] < left:
                    window.popleft() # 时间复杂度O(1)
                result.append(nums[window[0]])
        return result
