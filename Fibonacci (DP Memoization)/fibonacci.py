# Author: Jigesh Sheoran
# Last Modified : 27 / 02 / 2026
# Experiment: Fibonacci using Dynamic Programming (Memoization)

def fibonacci(n, memo):
    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


# user input
print("Fibonacci using DP (Memoization) Program")

n = int(input("Enter value of n:\n"))

# Base cases
memo = {0: 0, 1: 1}

result = fibonacci(n, memo)

print(f"\nFibonacci({n}) =", result)
print("Program executed successfully.")
