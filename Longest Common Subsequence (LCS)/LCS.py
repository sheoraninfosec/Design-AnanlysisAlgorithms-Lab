# Author: Jigesh Sheoran
# Last Modified : 28 / 02 / 2026
# Experiment: Longest Common Subsequence (LCS)

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct LCS string
    i, j = m, n
    lcs_string = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_string.reverse()

    return dp[m][n], "".join(lcs_string)


# user input
print("Longest Common Subsequence (LCS) Program")

X = input("Enter first string:\n")
Y = input("Enter second string:\n")

length, sequence = lcs(X, Y)

print("\nLength of LCS:", length)
print("LCS:", sequence)

print("Program executed successfully.")
