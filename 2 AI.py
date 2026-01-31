N = 8

# Function to print the chessboard
def print_board(board):
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# Function to check if placing queen is safe
def is_safe(board, row, col):
    for i in range(row):
        # Check column and diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

# Backtracking function
def solve_queens(board, row):
    if row == N:
        print_board(board)
        return True   # return False if you want all solutions

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, row + 1):
                return True
            board[row] = -1
    return False

# Main
board = [-1] * N
solve_queens(board, 0)
