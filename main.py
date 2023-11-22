def display_board(board):
    for row in board:
        print("|".join(row))


def check_winner(board, player):
    for i in range(1, len(board)):
        if all(board[i][j] == player for j in range(1, len(board[i]))) or \
           all(board[j][i] == player for j in range(1, len(board[i]))):  # проверить ряд и столбец
            return True

        if all(board[i][i] == player for i in range(1, len(board))) or \
           all(board[i][len(board) - i] == player for i in range(1, len(board))):  # проверить диагонали
            return True
    return False


def full_board(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def initialize_game():
    board_size = int(input("Укажите размер игрового поля (например, 2, 3, 4, т.д клетки): "))
    board = [[' ' for _ in range(board_size + 1)] for _ in range(board_size + 1)]
    for i in range(1, board_size + 1):
        board[0][i] = str(i-1)
        board[i][0] = str(i-1)
    current_player = 'X'
    while True:
        display_board(board)
        print(f"Ход игрока '{current_player}'")
        row = int(input("Выберите ряд: "))
        col = int(input("Выберите столбец: "))
        while row < 0 or row > board_size or col < 0 or col > board_size:
            print("Ошибка ввода. Повторите ещё раз.")
            display_board(board)
            row = int(input("Выберите ряд: "))
            col = int(input("Выберите столбец: "))
            continue
        if board[row+1][col+1] == ' ':
            board[row+1][col+1] = current_player
            if check_winner(board, current_player):
                display_board(board)
                print(f"Игрок '{current_player}' выиграл!")
                break
            elif full_board(board):
                display_board(board)
                print("У вас ничья!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Ячейка занята. Попробуйте другую.")


initialize_game()
