from collections import Counter
class Solution:
    show_subarrays = True
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        """
            用滑动窗口来维护小于<=k种类的子数组,通过窗口后缀计算总的子数组
            exactly(K) = at_most(K) - at_most(K-1)
        """
        def at_most(k_type:int):
            """
            计算最多包含k个不同整数的子数组数量
            """
            left = 0
            total = 0
            seen = Counter()
            for right,el in enumerate(nums):
                seen[el] += 1
                while len(seen) > k_type:
                    left_num = nums[left]
                    seen[left_num] -= 1
                    if seen[left_num] == 0:
                        del seen[left_num]
                    left += 1
                total += right - left + 1
                # 打印所有的子数组
                if self.show_subarrays  and k_type == k:
                    self.print_subarrays(nums, left, right, k_type)
            return total

        return at_most(k) - at_most(k-1)

    def print_subarrays(self, nums: list[int], left: int,right: int,k:int):
        while left <= right:
            els = nums[left:right + 1]
            if len(set(els)) == k:
                print(els,end = "  ")
            left += 1


if __name__ == '__main__':
    print(Solution().subarraysWithKDistinct([1,2,1,2,3], 2))
    print("-"*30)
    print(Solution().subarraysWithKDistinct([1,2,1,3,4], 3))