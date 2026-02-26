# Author: Jigesh Sheoran
# Last Modified : 26 / 02 / 2026
# Experiment: Naive Matrix Multiplication

def naive_matrix_multiply(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)

    # Initialize result matrix with zeros
    C = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]

    return C


# user input
print("Naive Matrix Multiplication Program")

n = int(input("Enter number of rows in Matrix A:\n"))
m = int(input("Enter number of columns in Matrix A:\n"))

print("Enter Matrix A row by row:")
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

p = int(input("Enter number of rows in Matrix B:\n"))
q = int(input("Enter number of columns in Matrix B:\n"))

if m != p:
    print("Matrix multiplication not possible. Columns of A must equal rows of B.")
else:
    print("Enter Matrix B row by row:")
    B = []
    for _ in range(p):
        B.append(list(map(int, input().split())))

    C = naive_matrix_multiply(A, B)

    print("\nResultant Matrix:")
    for row in C:
        print(row)

print("Program executed successfully.")
