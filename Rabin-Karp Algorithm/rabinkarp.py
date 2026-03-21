# Author: Jigesh Sheoran
# Last Modified : 20 / 03 / 2026
# Experiment: Rabin-Karp Algorithm (String Matching using Hashing)

def rabin_karp(text, pattern, d=256, q=101):
    n = len(text)
    m = len(pattern)
    h = pow(d, m-1) % q
    p = 0  # hash value for pattern
    t = 0  # hash value for text
    result = []

    # Initial hash calculation
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over text
    for i in range(n - m + 1):
        if p == t:
            # Check characters one by one (to avoid collision issues)
            if text[i:i+m] == pattern:
                result.append(i)

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q

            if t < 0:
                t += q

    return result


# user input
text = input("Enter text: ")
pattern = input("Enter pattern: ")

matches = rabin_karp(text, pattern)

if matches:
    print("\nPattern found at indices:", matches)
else:
    print("\nPattern not found.")

print("\nRabin-Karp Algorithm executed successfully.")
