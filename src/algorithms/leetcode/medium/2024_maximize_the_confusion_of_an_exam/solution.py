import functools


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # 使用functools.partial绑定target参数
        t_max_func = functools.partial(self._max_consecutive_answers, target='T')
        f_max_func = functools.partial(self._max_consecutive_answers, target='F')
        return max(t_max_func(answerKey=answerKey, k=k), f_max_func(answerKey=answerKey, k=k))

    @staticmethod
    def _max_consecutive_answers(*, target: str, answerKey: str, k: int) -> int:
        left = 0
        # 记录当前窗口不是target的个数
        curr = 0
        result = 0
        for right, val in enumerate(answerKey):
            if val != target:
                curr += 1
            while curr > k:
                curr -= 1 if answerKey[left] != target else 0
                left += 1
            result = max(result, right - left + 1)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxConsecutiveAnswers(answerKey="TTFF", k=2))
