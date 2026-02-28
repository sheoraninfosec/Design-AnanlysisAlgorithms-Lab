# Author: Jigesh Sheoran
# Last Modified : 28 / 02 / 2026
# Experiment: Edit Distance (Levenshtein Distance)

def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     # Delete
                    dp[i][j - 1],     # Insert
                    dp[i - 1][j - 1]  # Replace
                )

    return dp[m][n]


# user input
print("Edit Distance (Levenshtein Distance) Program")

str1 = input("Enter first string:\n")
str2 = input("Enter second string:\n")

result = edit_distance(str1, str2)

print("\nMinimum Edit Distance:", result)
print("Program executed successfully.")
