"""分数管理器 - 使用 dataclass 管理游戏分数"""
from dataclasses import dataclass, field


@dataclass
class ScoreManager:
    """
    分数管理器
    
    管理游戏分数的增加、重置和查询
    """
    _score: int = field(default=0, init=False, repr=False)
    
    @property
    def score(self) -> int:
        """获取当前分数"""
        return self._score
    
    def add_score(self, points: int = 1):
        """
        增加分数
        
        Args:
            points: 要增加的分数值，默认为 1
        """
        if points < 0:
            raise ValueError("分数增加值不能为负数")
        self._score += points
    
    def reset(self):
        """重置分数为 0"""
        self._score = 0
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"Score: {self._score}"
    
    def __repr__(self) -> str:
        """详细字符串表示"""
        return f"ScoreManager(score={self._score})"
