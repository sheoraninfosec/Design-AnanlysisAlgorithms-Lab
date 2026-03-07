# Author: Jigesh Sheoran
# Last Modififec : 08 / 02 / 2026
# Experiment: Sudoku Solver

def is_safe(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:

                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0

                return False
    return True


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


# main brain
print("Sudoku Solver Program")
print("Enter the Sudoku grid row by row (use 0 for empty cells):")

board = []
for _ in range(9):
    row = list(map(int, input().split()))
    board.append(row)

if solve_sudoku(board):
    print("\nSolved Sudoku:")
    print_board(board)
else:
    print("\nNo solution exists.")
