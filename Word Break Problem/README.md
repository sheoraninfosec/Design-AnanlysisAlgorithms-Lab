# Word Break Problem – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Word Break Problem** using **Dynamic Programming**.
The objective is to determine whether a given string can be segmented into one or more valid words from a provided dictionary.

---

## 🧠 Algorithm Concept

Let:

dp[i] = True if substring s[0:i] can be segmented into valid dictionary words

Initialization:

dp[0] = True

Recurrence Relation:

For each i from 1 to n:
If there exists j < i such that:

dp[j] = True  
and s[j:i] is in dictionary  

Then:

dp[i] = True

The final answer is:

dp[n]

---

## 💻 Sample Input 

```php
Enter the string:
leetcode
Enter dictionary words separated by space:
leet code
```

---

##💻 Expected Output

```php
The string CAN be segmented into dictionary words.
```
