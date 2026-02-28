# Edit Distance (Levenshtein Distance) – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Edit Distance (Levenshtein Distance)** algorithm using **Dynamic Programming**.
<br>The goal is to find the minimum number of operations required to convert one string into another.

Allowed operations:
- Insert
- Delete
- Replace

---

## 🧠 Algorithm Concept

Let:

dp[i][j] = Minimum edit distance between first i characters of str1 and first j characters of str2

Recurrence Relation:

If characters match:

dp[i][j] = dp[i-1][j-1]

Else:

dp[i][j] = 1 + min(
    dp[i-1][j],      // Delete
    dp[i][j-1],      // Insert
    dp[i-1][j-1]     // Replace
)

The final answer is stored in:

dp[m][n]

---

## 💻 Sample Input 

```php
Enter first string:
kitten
Enter second string:
sitting
```

---

## 💻 Expected Output

```php
Minimum Edit Distance: 3
```
