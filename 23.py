# Lex & Misi's Tic-Tac-Toe ❌⭕
# A simple 2-player Python game

board = [" " for _ in range(9)]  # 3x3 board


def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(symbol):
    # all winning positions
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == symbol:
            return True
    return False


def is_full():
    return " " not in board


def play_game():
    print("🎮 Welcome to Lex & Misi’s Tic-Tac-Toe!")
    print("Player 1 = X, Player 2 = O")
    print_board()

    turn = "X"

    while True:
        print(f"Player {turn}, choose your spot (1-9): ", end="")
        try:
            move = int(input()) - 1
        except ValueError:
            print("❌ Please enter a number between 1 and 9.")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("⚠️ Invalid move. Try again!")
            continue

        board[move] = turn
        print_board()

        if check_winner(turn):
            print(f"🏆 Player {turn} wins! Congratulations! 🎉")
            break
        elif is_full():
            print("😮 It’s a tie!")
            break

        # switch turns
        turn = "O" if turn == "X" else "X"


play_game()