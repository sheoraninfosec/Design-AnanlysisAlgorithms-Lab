# Longest Increasing Subsequence (LIS) – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Longest Increasing Subsequence (LIS)** problem using **Dynamic Programming**.

The objective is to find the length of the longest subsequence in a given sequence such that all elements of the subsequence are strictly increasing.
A subsequence does not need to be contiguous.

---

## 🧠 Algorithm Concept

Let:

dp[i] = Length of the longest increasing subsequence ending at index i

Recurrence Relation:

If arr[i] > arr[j] for j < i:

dp[i] = max(dp[i], dp[j] + 1)

The final answer is:

max(dp[i]) for all i

---

## 💻 Sample Input 

```php
Enter array elements separated by space:
10 22 9 33 21 50 41 60
```

---

## 💻 Expected Output

```php
Length of LIS: 5
```
