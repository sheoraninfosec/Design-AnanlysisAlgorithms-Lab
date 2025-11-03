# Author: Jigesh Sheoran
# SAPID: 590025428

import numpy as np

def read_matrix(n):
    
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return np.array(matrix)

def split(matrix):
    #split into 4 parts
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return (
        matrix[:row2, :col2],  # a11
        matrix[:row2, col2:],  # a12
        matrix[row2:, :col2],  # a21
        matrix[row2:, col2:],  # a22
    )

def strassen_multiply(x, y):
    
    if len(x) == 1:
        return x * y

    a, b, c, d = split(x)
    e, f, g, h = split(y)

    # 7 multiplications
    d1 = strassen_multiply(a + d, e + h)
    d2 = strassen_multiply(c + d, e)
    d3 = strassen_multiply(a, f - h)
    d4 = strassen_multiply(d, g - e)
    d5 = strassen_multiply(a + b, h)
    d6 = strassen_multiply(c - a, e + f)
    d7 = strassen_multiply(b - d, g + h)

    # Combining back
    c11 = d1 + d4 - d5 + d7
    c12 = d3 + d5
    c21 = d2 + d4
    c22 = d1 + d3 - d2 + d6

    return np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

def strassen(x, y):
    #padding
    n = x.shape[0]
    if n & (n - 1) == 0 and n != 0:
        return strassen_multiply(x, y)

    m = 1
    while m < n:
        m *= 2

    x_padded = np.zeros((m, m))
    y_padded = np.zeros((m, m))
    x_padded[:n, :n] = x
    y_padded[:n, :n] = y

    result_padded = strassen_multiply(x_padded, y_padded)
    return result_padded[:n, :n]


if __name__ == "__main__":
    n = int(input("Enter the size of Matrix: "))
    print("\nEnter elements for Matrix A:")
    A = read_matrix(n)
    print("\nEnter elements for Matrix B:")
    B = read_matrix(n)

    strassen_result = strassen(A, B)
    print("\nResult Strassen's Algo:\n", strassen_result)

    numpy_result = np.dot(A, B)
    print("\nResult from NumPy (for verification):\n", numpy_result)