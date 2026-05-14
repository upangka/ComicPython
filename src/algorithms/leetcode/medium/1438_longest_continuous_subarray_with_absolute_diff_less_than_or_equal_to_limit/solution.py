from dataclasses import dataclass
from heapq import heappush, heappop

debugger = False


@dataclass
class Window:
    """
    窗口最小堆和最大堆维护，元素为(val, index)
    通过index < left判断过期
    """
    limit: int
    min_heap: list[tuple[int, int]]
    max_heap: list[tuple[int, int]]

    def push(self, *, val: int, idx: int):
        """
        入窗
        """
        heappush(self.min_heap, (val, idx))
        heappush(self.max_heap, (-val, idx))

    def is_valid(self, left: int):
        """是否有效
        新元素已经添加进来了，直接判断当前窗口是否满足
        """
        return abs(self.min_heap[0][0] + self.max_heap[0][0]) <= self.limit

    def clean(self, left: int):
        """出窗
        清除过期的元素
        """
        while self.min_heap[0][1] < left:
            heappop(self.min_heap)
        while self.max_heap[0][1] < left:
            heappop(self.max_heap)


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        """
        出窗的元素如果是最大值或最小值，你需要知道**下一个最大值/最小值是谁**
        使用堆方便回溯
        """
        left = 0
        total = 0
        curr = Window(min_heap=[], max_heap=[], limit=limit)
        for right, val in enumerate(nums):
            curr.push(val=val, idx=right)
            while not curr.is_valid(left):
                left += 1
                curr.clean(left)
            total = max(total, right - left + 1)

        debugger and print(f"{curr.min_heap=} \n{curr.max_heap=}")
        return total


if __name__ == '__main__':
    solution = Solution()

    # 测试用例1: [8,2,4,7], limit=4
    result = solution.longestSubarray(nums=[8, 2, 4, 7], limit=4)
    assert result == 2, f"测试用例1失败: nums=[8,2,4,7], limit=4, 期望结果=2, 实际结果={result=}"

    # 测试用例2: [10,1,2,4,7,2], limit=5
    result = solution.longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5)
    assert result == 4, f"测试用例2失败: nums=[10,1,2,4,7,2], limit=5, 期望结果=4, 实际结果={result}"

    # 测试用例3: [4,2,2,2,4,4,2,2], limit=0
    result = solution.longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0)
    assert result == 3, f"测试用例3失败: nums=[4,2,2,2,4,4,2,2], limit=0, 期望结果=3, 实际结果={result}"

    # 测试用例4: [2,5,2], limit=9
    result = solution.longestSubarray(nums=[2, 5, 2], limit=9)
    assert result == 3, f"测试用例4失败: nums[2,5,2], limit=9, 期望结果=3, 实际结果={result}"

    print("所有测试用例通过！")
