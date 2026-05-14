
from dataclasses import dataclass

@dataclass
class Window:
    """
    or_result: 维护各个元素bit位有1只占据指定位置，用于快速判断是否冲突
    由于需要使用or_result判断冲突，所以先判断收缩，最后再入窗
    """
    or_result: int = 0

    def push(self,val: int):
        """入窗"""
        self.or_result |= val

    def is_valid(self,target: int):
        """检查"""
        return self.or_result & target == 0

    def pop(self,val: int):
        """出窗"""
        self.or_result ^= val

class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        left = 0
        curr = Window()
        total = 0
        for right,val in enumerate(nums):
            """
            为了维护窗口里面的元素两两相与都是0
            这里先进行收缩，最后在扩展，是为了方便检查是否重复1bit位
            """
            while not curr.is_valid(val):
                curr.pop(nums[left])
                left += 1
            curr.push(val)
            total = max(total,right - left + 1)
        return total


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestNiceSubarray(nums = [1,3,8,48,10]))
    print(solution.longestNiceSubarray(nums = [3,1,5,11,13]))
