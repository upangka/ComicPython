class WizCoin:
    """一种虚构的魔法货币

    基于《哈利·波特》系列的货币系统：
        - Galleons（加隆）：最高面值，金币
        - Sickles（西可）：中等面值，银币
        - Knuts（纳特）：最小面值，铜币

    兑换关系：
        1 加隆 = 17 西可
        1 西可 = 29 纳特
        1 加隆 = 493 纳特
    """

    def __init__(self, galleons, sickles, knuts):
        """初始化 WizCoin 实例

        Args:
            galleons (int): 加隆数量（金币）
            sickles (int): 西可数量（银币）
            knuts (int): 纳特数量（铜币）
        """
        self.galleons = galleons  # 加隆（最高面值，金币）
        self.sickles = sickles  # 西可（中等面值，银币）
        self.knuts = knuts  # 纳特（最小面值，铜币）
