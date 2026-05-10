class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        def dfs(path: list[int], remain_nums: list[int]):
            if len(path) == len(nums):
                res.append(path[:])
                return

            # 同层方法栈，都创建一个set，来进行剪枝
            used = set()
            for i, el in enumerate(remain_nums):
                if el in used:
                    continue
                used.add(el)
                dfs(path + [el], remain_nums[:i] + remain_nums[i + 1:])

        dfs([], nums)
        return res

if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 2]))