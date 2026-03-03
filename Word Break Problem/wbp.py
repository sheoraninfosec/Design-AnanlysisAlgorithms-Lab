# Author: Jigesh Sheoran
# Last Modifed : 03 / 03 / 2026
# Experiment: Word Break Problem

def word_break(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]


# user input
print("Word Break Problem Program")

s = input("Enter the string:\n")
dictionary = input("Enter dictionary words separated by space:\n").split()

result = word_break(s, set(dictionary))

if result:
    print("\nThe string CAN be segmented into dictionary words.")
else:
    print("\nThe string CANNOT be segmented into dictionary words.")

print("Program executed successfully.")
