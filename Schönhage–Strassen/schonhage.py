# Author: Jigesh Sheoran
# Last Modified : 24/02/2026
# Experiment: Schönhage–Strassen Algorithm (FFT-Based Integer Multiplication)

import numpy as np
import math

def fft_multiply(a, b):
    n = len(a) + len(b) - 1
    size = 1 << (n - 1).bit_length()   # Next power of 2

    A = np.fft.fft(a, size)
    B = np.fft.fft(b, size)

    C = A * B
    result = np.fft.ifft(C)

    return np.round(result.real).astype(int)

def multiply_large_integers(x, y):
    # Convert integers to reversed digit lists
    a = list(map(int, str(x)))[::-1]
    b = list(map(int, str(y)))[::-1]

    # Multiply using FFT
    result = fft_multiply(a, b)

    # Convert numpy array to list
    result = result.tolist()

    # Handle carry
    carry = 0
    for i in range(len(result)):
        total = result[i] + carry
        result[i] = total % 10
        carry = total // 10

    # Remove leading zeros safely
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    # Convert back to integer
    return int(''.join(map(str, result[::-1])))

# user input
x = int(input("Enter first large integer: "))
y = int(input("Enter second large integer: "))

product = multiply_large_integers(x, y)

print("\nProduct:", product)
print("\nSchönhage–Strassen (FFT-Based) executed successfully.")
