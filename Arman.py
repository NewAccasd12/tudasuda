def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Проверяем строки, столбцы и диагонали
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves_left = 9

    while moves_left > 0:
        print_board(board)
        row = int(input(f"Игрок {current_player}, введите номер строки (0-2): "))
        col = int(input(f"Игрок {current_player}, введите номер столбца (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            moves_left -= 1
            if check_winner(board):
                print_board(board)
                print(f"Игрок {current_player} победил!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Эта клетка уже занята. Попробуйте снова.")

    if moves_left == 0:
        print("Ничья!")
        print_board(board)

tic_tac_toe()
