from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return list(permutations(nums))

if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))