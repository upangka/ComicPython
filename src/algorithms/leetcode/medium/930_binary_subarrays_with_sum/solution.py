class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """
        exactly(K) = at_most(K) - at_most(K-1)
        """

        def at_most(target: int):
            """
            维护窗口当窗口内的所有元素之和等于2时，代表这个窗口的子数组有等于0，等于1，等于2的，
            也就是说窗口中`<=2` 的子数组总数,(right - left + 1)**后缀计算**。
            """
            # 数组根本本存在和小于0的情况
            if target < 0: return 0
            left = 0
            window_sum = 0
            result = 0
            for right, num in enumerate(nums):
                window_sum += num
                while window_sum > target:
                    window_sum -= nums[left]
                    left += 1
                result += right - left + 1
            return result

        # goal为0要特殊处理一下，因为元素只有0和1，所以窗口维护0,本身就0的范围，不需要减
        # return at_most(goal) - at_most(goal - 1) if goal else at_most(goal)
        return at_most(goal) - at_most(goal - 1)


if __name__ == '__main__':
    solution = Solution()

    # 测试用例1: [1,0,1,0,1], goal=2, 期望输出4
    # 和为2的子数组: [1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1]
    assert solution.numSubarraysWithSum([1, 0, 1, 0, 1], 2) == 4, "测试用例1失败"

    # 测试用例2: [0,0,0,0,0], goal=0, 期望输出15
    # 所有子数组的和都是0，共5*(5+1)/2=15个
    assert solution.numSubarraysWithSum([0, 0, 0, 0, 0], 0) == 15, "测试用例2失败"

    # 测试用例3: [1,1,1,1,1], goal=3, 期望输出3
    # 和为3的子数组: [1,1,1](位置0-2), [1,1,1](位置1-3), [1,1,1](位置2-4)
    assert solution.numSubarraysWithSum([1, 1, 1, 1, 1], 3) == 3, "测试用例3失败"

    print("所有测试用例通过！")
