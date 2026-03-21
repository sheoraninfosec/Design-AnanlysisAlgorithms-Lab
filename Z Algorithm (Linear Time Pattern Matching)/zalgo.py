# Author: Jigesh Sheoran
# Last Modified : 21 / 03 / 2026
# Experiment: Z Algorithm (Linear Time Pattern Matching)

def compute_z_array(s):
    n = len(s)
    Z = [0] * n
    L, R = 0, 0

    for i in range(1, n):
        if i <= R:
            Z[i] = min(R - i + 1, Z[i - L])

        while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
            Z[i] += 1

        if i + Z[i] - 1 > R:
            L, R = i, i + Z[i] - 1

    return Z


def z_algorithm_search(text, pattern):
    concat = pattern + "$" + text
    Z = compute_z_array(concat)
    m = len(pattern)
    result = []

    for i in range(len(Z)):
        if Z[i] == m:
            result.append(i - m - 1)

    return result


# user input
text = input("Enter text: ")
pattern = input("Enter pattern: ")

matches = z_algorithm_search(text, pattern)

if matches:
    print("\nPattern found at indices:", matches)
else:
    print("\nPattern not found.")

print("\nZ Algorithm executed successfully.")
