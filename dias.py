import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = ""
    while player not in ["X", "O"]:
        player = input("Фигураны таңдаңыз (X немесе O): ").upper()
    
    ai_player = "O" if player == "X" else "X"
    print(f"Сіз {player} таңдадыңыз, бот {ai_player} болады.")
    
    turn = 0 if player == "X" else 1
    
    while True:
        print_board(board)
        current_player = player if turn % 2 == 0 else ai_player
        
        if current_player == player:
            valid_input = False
            while not valid_input:
                try:
                    row, col = map(int, input("Координаталарды енгізіңіз (0-2 аралығы, қатар, баған): ").split())
                    if board[row][col] == " ":
                        valid_input = True
                    else:
                        print("Бұл орын бос емес. Басқа орын таңдаңыз.")
                except (ValueError, IndexError):
                    print("Қате енгізу! 0 мен 2 арасындағы екі сан енгізіңіз.")
        else:
            row, col = random.choice(get_empty_cells(board))
            print(f"Бот ({ai_player}) жүріс жасады: {row} {col}")
        
        board[row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} жеңді!")
            break
        if not get_empty_cells(board):
            print_board(board)
            print("Тең ойын!")
            break
        
        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
