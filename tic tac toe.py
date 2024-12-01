import random

# Constants for the two players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in range(3):
        if all([board[row][col] == player for col in range(3)]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Check if the board is full (no empty spaces left)
def is_full(board):
    return all([cell != EMPTY for row in board for cell in row])

# Minimax algorithm to find the best move for AI (Player O)
def minimax(board, depth, is_maximizing):
    # If the AI wins or the player wins, return respective score
    if check_winner(board, PLAYER_O):
        return 1  # AI wins
    if check_winner(board, PLAYER_X):
        return -1  # Player X wins
    if is_full(board):
        return 0  # Tie

    # Maximizing (AI's turn) vs Minimizing (Player X's turn)
    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    score = minimax(board, depth + 1, False)
                    board[row][col] = EMPTY
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    score = minimax(board, depth + 1, True)
                    board[row][col] = EMPTY
                    best_score = min(best_score, score)
        return best_score

# Find the best move for AI using minimax
def best_move(board):
    best_score = -float('inf')
    move = (-1, -1)

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_O
                score = minimax(board, 0, False)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n".join(["|".join(row) for row in board]))
    print()

# Function to handle the player's move
def player_move(board):
    while True:
        try:
            move = input("Enter your move (row,col) e.g. 1,1 for the center: ")
            row, col = map(int, move.split(","))
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                break
            else:
                print("This space is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid move. Please enter row,col in the format 0-2,0-2.")

# Main game loop
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player X (Human) move
        player_move(board)
        print_board(board)
        
        if check_winner(board, PLAYER_X):
            print("Player X (You) win!")
            break
        if is_full(board):
            print("It's a tie!")
            break
        
        # Player O (AI) move
        print("AI (Player O) is making its move...")
        row, col = best_move(board)
        board[row][col] = PLAYER_O
        print_board(board)
        
        if check_winner(board, PLAYER_O):
            print("AI (Player O) wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

# Start the game
play_game()
