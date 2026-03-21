# Author: Jigesh Sheoran
# Last Modified : 18 / 03 / 2026
# Experiment: Boyer-Moore Algorithm (Efficient String Matching)

def bad_character_heuristic(pattern):
    bad_char = [-1] * 256
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i
    return bad_char


def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)

    bad_char = bad_character_heuristic(pattern)
    result = []

    s = 0  # shift of pattern

    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            result.append(s)
            s += (m - bad_char[ord(text[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(text[s + j])])

    return result


# user input
text = input("Enter text: ")
pattern = input("Enter pattern: ")

matches = boyer_moore(text, pattern)

if matches:
    print("\nPattern found at indices:", matches)
else:
    print("\nPattern not found.")

print("\nBoyer-Moore Algorithm executed successfully.")
