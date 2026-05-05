from dataclasses import dataclass


@dataclass(frozen=True)
class GoldMine:
    """金矿数据模型"""
    name: str  # 金矿名称
    gold: int  # 黄金产量(公斤)
    workers_needed: int  # 所需工人数


class Solution:
    def find_max_gold(self, gold_mines: list[GoldMine], workers: int) -> int:
        """
        使用动态规划求解0/1背包问题 - 国王金矿问题
        
        Args:
            gold_mines: 金矿列表，每个金矿包含名称、黄金产量和所需工人数
            workers: 可用的工人总数
            
        Returns:
            int: 能够获得的最大黄金产量（公斤）
        """
        dp = [[0] * (workers + 1) for _ in range(len(gold_mines) + 1)]
        for i in range(1, len(gold_mines) + 1):
            gold_mine = gold_mines[i - 1]
            for w in range(1, workers + 1):
                if gold_mine.workers_needed > w:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(gold_mine.gold + dp[i - 1][w - gold_mine.workers_needed],
                                   dp[i - 1][w])
        # [print(row) for row in dp]
        return dp[-1][-1]


if __name__ == '__main__':
    gold_mines = [
        GoldMine(name='金矿1', gold=400, workers_needed=5),
        GoldMine(name='金矿2', gold=500, workers_needed=5),
        GoldMine(name='金矿3', gold=200, workers_needed=3),
        GoldMine(name='金矿4', gold=300, workers_needed=4),
        GoldMine(name='金矿5', gold=350, workers_needed=3),
    ]
    print(Solution().find_max_gold(gold_mines, 10))
