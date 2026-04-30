# 井字棋棋盘字典key
ALL_SPACES = [str(i) for i in range(1, 10)]
# 字符串常量
X, O, BLANK = 'X', 'O', ' '


class TTTBoard:
    """井字棋游戏"""

    def __init__(self):
        """初始化棋盘"""
        self._spaces = {space: BLANK for space in ALL_SPACES}

    def is_valid_space(self, space) -> bool:
        """判断是否为有效的移动
        Args:
            space: 要检查的位置，应该是 '1' 到 '9' 的字符串
        Returns:
            bool: 如果该位置为空则返回 True，否则返回 False
        """
        return space in ALL_SPACES and self._spaces[space] == BLANK

    def is_winner(self, player):
        """判断玩家是否获胜"""
        s, p = self._spaces, player  # 简写

        # 检查3行，3列，2对角线上的标记
        return (s['1'] == s['2'] == s['3'] == p or
                s['4'] == s['5'] == s['6'] == p or
                s['7'] == s['8'] == s['9'] == p or
                s['1'] == s['4'] == s['7'] == p or
                s['2'] == s['5'] == s['8'] == p or
                s['3'] == s['6'] == s['9'] == p or
                s['1'] == s['5'] == s['9'] == p or
                s['3'] == s['5'] == s['7'] == p)

    def is_board_full(self) -> bool:
        """判断棋盘是否已满
         Returns:
            bool: 如果棋盘已满返回 True，否则返回 False
        """
        return not any(space == BLANK for space in self._spaces.values())

    def update_board(self, space, player):
        """更新棋盘
        Args:
            space: 要更新的位置，应该是 '1' 到 '9' 的字符串
            player: 要更新位置的玩家，应该是 'X' 或 'O'
        """
        self._spaces[space] = player

    def __str__(self):
        """返回棋盘字符串"""
        return f"""
            {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']}  1 2 3
            -+-+-
            {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']}  4 5 6
            -+-+-
            {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']}  7 8 9
            """

    __repr__ = __str__


class MiniBoard(TTTBoard):
    """小棋盘"""
    def __str__(self):
        s = {
            space: '.' if val == BLANK else val
            for space, val in self._spaces.items()
        }
        """返回棋盘字符串"""
        return f"""
                    {s['1']}{s['2']}{s['3']}  1 2 3
                    {s['4']}{s['5']}{s['6']}  4 5 6
                    {s['7']}{s['8']}{s['9']}  7 8 9
                    """

    __repr__ = __str__
