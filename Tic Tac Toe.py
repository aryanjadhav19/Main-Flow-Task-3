import random

# Constants
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Minimax Algorithm to determine the best move for the AI
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return -10 + depth  # Player wins
    elif winner == PLAYER_O:
        return 10 - depth  # AI wins
    elif is_board_full(board):
        return 0  # Draw

    if is_maximizing:  # AI's turn
        best_score = -float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                score = minimax(board, depth + 1, False)
                board[i] = EMPTY
                best_score = max(score, best_score)
        return best_score
    else:  # Player's turn
        best_score = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                score = minimax(board, depth + 1, True)
                board[i] = EMPTY
                best_score = min(score, best_score)
        return best_score

# Function to determine the best move for AI using minimax
def best_move(board):
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_O
            score = minimax(board, 0, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    return move

# Check if the board is full
def is_board_full(board):
    return all([spot != EMPTY for spot in board])

# Check for a winner
def check_winner(board):
    # Check rows, columns, and diagonals
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != EMPTY:
            return board[condition[0]]
    return None  # No winner

# Print the game board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Main game loop
def play_game():
    board = [EMPTY] * 9
    current_player = PLAYER_X  # Player starts first

    while True:
        print_board(board)

        if current_player == PLAYER_X:
            # Player's turn
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == EMPTY:
                board[move] = PLAYER_X
                if check_winner(board):
                    print_board(board)
                    print("You win!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                current_player = PLAYER_O
            else:
                print("Invalid move, try again.")
        else:
            # AI's turn
            print("AI is making its move...")
            move = best_move(board)
            board[move] = PLAYER_O
            if check_winner(board):
                print_board(board)
                print("AI wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = PLAYER_X

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    play_game()