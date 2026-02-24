# Author: Jigesh Sheoran
# Last Modified : 24/02/2026

import numpy as np

# FFT Polynomial Multiplication
def fft_multiply(a, b):
    n = len(a) + len(b) - 1
    size = 1 << (n - 1).bit_length()

    A = np.fft.fft(a, size)
    B = np.fft.fft(b, size)

    C = A * B
    result = np.fft.ifft(C)

    return np.round(result.real).astype(int)


# user Input 
print("Enter first polynomial coefficients:")
a = list(map(int, input().split()))

print("Enter second polynomial coefficients:")
b = list(map(int, input().split()))

result = fft_multiply(a, b)

print("\nPolynomial Multiplication Result:")
print(result[:len(a)+len(b)-1])
