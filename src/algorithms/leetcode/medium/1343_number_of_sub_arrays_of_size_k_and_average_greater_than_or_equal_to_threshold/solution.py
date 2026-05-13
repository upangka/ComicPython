class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        target = k * threshold
        curr = sum(arr[:k])
        cnt = 1 if curr >= target else 0
        for i in range(k, len(arr)):
            curr += arr[i] - arr[i - k]
            cnt += 1 if curr >= target else 0
        return cnt
