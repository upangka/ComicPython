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


class HintBoard(TTTBoard):
    """添加说明X和O是否只差一步胜利"""

    def __str__(self):
        msgs = [super().__str__()]
        if self._judge_next_win(X):
            msgs.append(f"{X}的下一步能获胜")
        if self._judge_next_win(O):
            msgs.append(f"{O}的下一步能获胜")
        return '\n'.join(msgs)

    def _judge_next_win(self, player):
        """判断玩家在下一步是否能获胜（通过模拟尝试每个空位）

        Args:
            player: 要检查的玩家，应该是 'X' 或 'O'

        Returns:
            bool: 如果玩家能在下一步获胜返回 True，否则返回 False
        """
        origin_space = self._spaces.copy()  # 保存原始棋盘状态用于恢复
        is_win = False
        for space in self._spaces.keys():
            if self._spaces[space] == BLANK:  # 只检查空位
                super().update_board(space, player)  # 模拟在该位置落子
                if self.is_winner(player):
                    is_win = True
                    break
                super().update_board(space, BLANK)  # 恢复该位置为空位，尝试下一个位置
        self._spaces = origin_space  # 恢复原始棋盘状态
        return is_win


class HybridBoard(HintBoard,MiniBoard):
    """mini棋盘拥有提示功能"""
    pass