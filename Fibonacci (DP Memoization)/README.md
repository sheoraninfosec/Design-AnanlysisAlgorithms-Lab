# Fibonacci (DP / Memoization) – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Fibonacci sequence** using **Dynamic Programming (Memoization)**.
The Fibonacci series is defined as:

F(n) = F(n-1) + F(n-2)

Instead of recalculating values repeatedly (as in naive recursion), memoization stores previously computed values to improve efficiency.

---

## 🧠 Algorithm Concept

The algorithm works as follows:

1. Define base cases:
   - F(0) = 0
   - F(1) = 1
2. Store computed Fibonacci values in a dictionary (memo).
3. Before computing F(n), check if it is already stored.
4. If stored → return value.
5. Otherwise → compute and store it.

This avoids repeated subproblem computation.

---

## ⏱ Space Complexity: O(n)

Naive recursive approach takes O(2^n).

---

## 💻 Sample Input 

```php
Enter value of n:
7
```
