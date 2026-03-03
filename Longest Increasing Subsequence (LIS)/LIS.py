# Author: Jigesh Sheoran
# Last Modified : 02 / 03 / 2026
# Experiment: Longest Increasing Subsequence (LIS)

def lis(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# user input
print("Longest Increasing Subsequence (LIS) Program")

arr = list(map(int, input("Enter array elements separated by space:\n").split()))

result = lis(arr)

print("\nLength of LIS:", result)
print("Program executed successfully.")
