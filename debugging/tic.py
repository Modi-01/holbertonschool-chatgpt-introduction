#!/usr/bin/python3


def print_board(board):
    """Print the current tic-tac-toe board."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)


def check_winner(board):
    """
    Return the winner symbol ('X' or 'O') if there is a winner, otherwise None.
    """
    # Rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return row[0]

    # Columns
    for col in range(len(board[0])):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # Diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


def board_full(board):
    """Return True if no empty spaces remain."""
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if row not in (0, 1, 2) or col not in (0, 1, 2):
            print("Invalid position. Row and column must be 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner is not None:
            print_board(board)
            print("Player " + winner + " wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"


tic_tac_toe()
