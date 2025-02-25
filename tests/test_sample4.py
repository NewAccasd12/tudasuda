import pytest

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

def test_check_winner():
    board_x_win = [
        ["X", "X", "X"],
        [" ", "O", " "],
        ["O", " ", " "]
    ]
    board_o_win = [
        ["X", "O", "X"],
        ["X", "O", " "],
        [" ", "O", "X"]
    ]
    board_no_win = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"]
    ]
    
    print("Тест 1: X жеңуі керек:", check_winner(board_x_win, "X") == True)
    print("Тест 2: O жеңбеуі керек:", check_winner(board_x_win, "O") == False)
    print("Тест 3: O жеңуі керек:", check_winner(board_o_win, "O") == True)
    print("Тест 4: X жеңбеуі керек:", check_winner(board_o_win, "X") == False)
    print("Тест 5: Ешкім жеңбеуі керек:", check_winner(board_no_win, "X") == False)
    print("Тест 6: Ешкім жеңбеуі керек:", check_winner(board_no_win, "O") == False)

def test_get_empty_cells():
    board = [
        ["X", "O", " "],
        ["X", "O", " "],
        [" ", " ", "X"]
    ]
    empty_cells = get_empty_cells(board)
    
    print("Бос орын саны:", len(empty_cells) == 4)
    print("Тест 7: (0,2) бар ма:", (0, 2) in empty_cells)
    print("Тест 8: (1,2) бар ма:", (1, 2) in empty_cells)
    print("Тест 9: (2,0) бар ма:", (2, 0) in empty_cells)
    print("Тест 10: (2,1) бар ма:", (2, 1) in empty_cells)

if __name__ == "__main__":
    test_check_winner()
    test_get_empty_cells() 