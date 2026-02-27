# 0/1 Knapsack – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **0/1 Knapsack problem** using **Dynamic Programming (Tabulation method)**.
In the 0/1 Knapsack problem, each item can either be included (1) or excluded (0). 
The goal is to maximize total value without exceeding the given capacity.

---

## 🧠 Algorithm Concept

Let:
dp[i][w] = Maximum value using first i items with capacity w

Recurrence Relation:

If weight[i] ≤ w:
dp[i][w] = max(value[i] + dp[i-1][w-weight[i]], dp[i-1][w])

Else:
dp[i][w] = dp[i-1][w]

The final answer is stored in:
dp[n][capacity]

---

## 💻 Sample Input 

```php
Enter number of items:
3
Enter weights separated by space:
10 20 30
Enter values separated by space:
60 100 120
Enter knapsack capacity:
50
```
