# Author: Jigesh Sheoran
# Last Modified: 17/02/2026

import numpy as np
import time

def conventional_multiply(A, B):
    return np.dot(A, B)

def strassen(A, B):
    n = len(A)
    if n == 1:
        return A * B
    mid = n // 2

    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    return np.vstack((top, bottom))


# User Input 
n = int(input("Enter size of square matrices (power of 2): "))

print("Enter Matrix A:")
A = []
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

print("Enter Matrix B:")
B = []
for i in range(n):
    row = list(map(float, input().split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

# time comparison
start = time.time()
C1 = conventional_multiply(A, B)
t1 = time.time() - start

start = time.time()
C2 = strassen(A, B)
t2 = time.time() - start

print("\nConventional Multiplication Result:\n", C1)
print("\nStrassen Multiplication Result:\n", C2)

print("\nTime Conventional:", t1)
print("Time Strassen:", t2)
