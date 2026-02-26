# Author: Jigesh Sheoran
# Last Modified : 26 / 02 / 2026
# Experiment: Naive String Matching

def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append(i)

    return positions


# user input
print("Naive String Matching Program")

text = input("Enter the text string:\n")
pattern = input("Enter the pattern to search:\n")

result = naive_string_match(text, pattern)

if result:
    print("Pattern found at positions:", result)
else:
    print("Pattern not found.")

print("Program executed successfully.")
