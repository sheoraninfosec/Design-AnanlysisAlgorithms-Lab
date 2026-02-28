# Longest Common Subsequence (LCS) – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Longest Common Subsequence (LCS)** problem using **Dynamic Programming**.
The goal is to find the longest subsequence that appears in both given strings. A subsequence does not need to be contiguous but must maintain relative order.

---

## 🧠 Algorithm Concept

Let:

dp[i][j] = Length of LCS of first i characters of X and first j characters of Y

Recurrence Relation:

If X[i-1] == Y[j-1]:

dp[i][j] = 1 + dp[i-1][j-1]

Else:

dp[i][j] = max(dp[i-1][j], dp[i][j-1])

The final answer is stored in:

dp[m][n]

Backtracking is used to reconstruct the LCS string.

---

## 💻 Sample Input 

```php
Enter first string:
BDCABA
Enter second string:
ABCBDAB
```

---

## 💻 Expected Output

```php
Length of LCS: 4
LCS: BCBA
```
