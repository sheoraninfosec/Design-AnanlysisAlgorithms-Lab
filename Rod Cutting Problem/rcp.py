# Author: Jigesh Sheoran
# Last Modifed : 03 / 03 / 2026
# Experiment: Rod Cutting Problem

def rod_cutting(prices, n):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(i):
            max_val = max(max_val, prices[j] + dp[i - j - 1])
        dp[i] = max_val

    return dp[n]


# user input
print("Rod Cutting Problem Program")

n = int(input("Enter length of rod:\n"))
prices = list(map(int, input("Enter prices for each length from 1 to n:\n").split()))

if len(prices) != n:
    print("Error: Number of prices must be equal to rod length.")
else:
    result = rod_cutting(prices, n)
    print("\nMaximum Obtainable Profit:", result)

print("Program executed successfully.")
