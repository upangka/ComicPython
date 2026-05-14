class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        """
        exactly(K) = at_most(K) - at_most(K-1)
        """
        def at_most(target: int):
            """
            维护窗口当窗口内奇数的个数,如target = 2 代表统计窗口下奇数为0,1,2的所有个数
            """
            left = 0
            total = 0
            # 窗口中计数的个数
            curr = 0
            for right,num in enumerate(nums):
                if self.is_odd(num):
                    curr += 1
                while curr > target:
                    if self.is_odd(nums[left]):
                        curr -= 1
                    left += 1
                total += right - left + 1
            return total
        return at_most(k) - at_most(k-1)

    @staticmethod
    def is_odd(num: int):
        return (num & 1) == 1


if __name__ == '__main__':
    solution = Solution()
    
    # 测试用例1: [1,1,2,1,1], k=3, 期望输出2
    # 恰好包含3个奇数的子数组: [1,1,2,1], [1,2,1,1]
    assert solution.numberOfSubarrays([1, 1, 2, 1, 1], 3) == 2, "测试用例1失败"
    
    # 测试用例2: [2,4,6], k=1, 期望输出0
    # 没有奇数，不存在包含1个奇数的子数组
    assert solution.numberOfSubarrays([2, 4, 6], 1) == 0, "测试用例2失败"
    
    # 测试用例3: [2,2,2,1,2,2,1,2,2,2], k=2, 期望输出16
    # LeetCode官方测试用例
    assert solution.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) == 16, "测试用例3失败"
    
    # 测试用例4: [1,1,1,1,1], k=1, 期望输出5
    # 每个单独的1都是一个子数组
    assert solution.numberOfSubarrays([1, 1, 1, 1, 1], 1) == 5, "测试用例4失败"
    
    print("所有测试用例通过！")