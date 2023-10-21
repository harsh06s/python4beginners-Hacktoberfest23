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

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row, col = map(int, input(f"Player {current_player}, enter row and column (e.g., 1 2): ").split())
        if board[row - 1][col - 1] == " ":
            board[row - 1][col - 1] = current_player
        else:
            print("That spot is already taken. Try again.")
            continue

        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
