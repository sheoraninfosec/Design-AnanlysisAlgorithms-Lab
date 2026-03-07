# Author: Jigesh Sheoran
# SAP ID: 590025428
# Experiment: N-Queens Problem (All Solutions)
# Course: M.Sc. Cyber Security – Semester 1

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check left diagonal
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_nqueens(n, row, board, solutions):
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)


def print_solution(board):
    n = len(board)
    for i in range(n):
        row = ["Q" if board[i] == j else "." for j in range(n)]
        print(" ".join(row))
    print()


# -----------------------------
# Main Program
# -----------------------------
print("N-Queens Problem (All Solutions)")

n = int(input("Enter value of N:\n"))

board = [-1] * n
solutions = []

solve_nqueens(n, 0, board, solutions)

print(f"\nTotal Solutions for N = {n}: {len(solutions)}\n")

for i, sol in enumerate(solutions, 1):
    print(f"Solution {i}:")
    print_solution(sol)

print("Program executed successfully.")
