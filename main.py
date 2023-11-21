def display_board(board):  # создать игровое поле
    for row in board:
        print("|".join(row))


def check_winner(board):  # проверить, есть ли победитель
    for i in range(1, 4):
        if board[i][1] == board[i][2] == board[i][3] != ' ' or \
           board[1][i] == board[2][i] == board[3][i] != ' ':
            return True
        if board[1][1] == board[2][2] == board[3][3] != ' ' or \
           board[1][3] == board[2][2] == board[3][1] != ' ':
            return True
    return False


def full_board(board):  # проверить свободные ячейки
    for row in board:
        if ' ' in row:
            return False
    return True


def initialize_game():  # запуск игры
    board = [[' ' for _ in range(4)] for _ in range(4)]
    for i in range(1, 4):
        board[0][i] = str(i-1)
        board[i][0] = str(i-1)
    current_player = 'X'

    while True:
        display_board(board)
        print(f"Ход игрока '{current_player}'")
        row = int(input("Выберите ряд 0, 1, или 2: "))
        col = int(input("Выберите столбец 0, 1, или 2: "))
        while row < 0 or row > 2 or col < 0 or col > 2:
            print("Ошибка ввода. Повторите ещё раз.")
            row = int(input("Выберите ряд 0, 1, или 2: "))
            col = int(input("Выберите столбец 0, 1, или 2: "))
            continue
        if board[row+1][col+1] == ' ':
            board[row+1][col+1] = current_player
            if check_winner(board):
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
