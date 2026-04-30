from tictactoe_oop import (TTTBoard, X, O, MiniBoard)


def run():
    print("Welcome to tic-tac-toe")
    if input("是否使用小棋盘？(y/n): ").lower() == 'y':
        board = MiniBoard()
    else:
        board = TTTBoard()
    current_player, next_player = X, O  # X先行，O后行

    while True:
        print(board)
        move = None
        while not board.is_valid_space(move):
            print(f"{current_player}请选择移动: (1-9)")
            move = input("> ")

        board.update_board(move, current_player)  # 执行移动

        # 检查游戏是否结束
        if board.is_winner(current_player):  # 首先检查一方是否获胜
            print(board)
            print(f"{current_player} 获胜！")
            break
        elif board.is_board_full():  # 检查棋盘是否已满
            print(board)
            print("平局")
            break

        current_player, next_player = next_player, current_player  # 交换玩家
    print("游戏结束")


if __name__ == '__main__':
    run()
