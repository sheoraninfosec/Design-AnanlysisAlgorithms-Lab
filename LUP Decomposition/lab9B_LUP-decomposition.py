# Author: Jigesh Sheoran
# Last Modified: 17/02/2026

import numpy as np
def lup_decomposition(A):
    n = len(A)
    A = A.copy()
    P = np.identity(n)

    for i in range(n):
        pivot = np.argmax(abs(A[i:, i])) + i

        if A[pivot, i] == 0:
            raise ValueError("Matrix is singular")

        # Swap rows
        A[[i, pivot]] = A[[pivot, i]]
        P[[i, pivot]] = P[[pivot, i]]

        for j in range(i+1, n):
            A[j, i] /= A[i, i]
            A[j, i+1:] -= A[j, i] * A[i, i+1:]

    L = np.tril(A, -1) + np.identity(n)
    U = np.triu(A)
    return L, U, P


# user input 
n = int(input("\nEnter size of square matrix for LUP: "))

print("Enter matrix elements row by row:")
A = []
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

A = np.array(A)
L, U, P = lup_decomposition(A)

print("\nL Matrix:\n", L)
print("\nU Matrix:\n", U)
print("\nP Matrix:\n", P)

print("\nVerification (P*A = L*U):")
print(np.dot(P, A))
print(np.dot(L, U))
