class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr = sum(nums[:k])
        best = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            best = max(best, curr)
        return best / k


if __name__ == '__main__':
    print(Solution().findMaxAverage([0, 4, 0, 3, 2], 1))
