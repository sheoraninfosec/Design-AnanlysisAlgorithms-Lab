# Coin Change Problem – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Coin Change Problem** using **Dynamic Programming**.

The objective is to determine the minimum number of coins required to make a given target amount using provided coin denominations.

Each coin can be used multiple times.

---

## 🧠 Algorithm Concept

Let:

dp[i] = Minimum number of coins required to make amount i

Initialize:

dp[0] = 0  
dp[i] = ∞ for all i > 0

Recurrence Relation:

dp[i] = min(dp[i], dp[i - coin] + 1)

The final answer is stored in:

dp[amount]

If dp[amount] remains infinity, the amount cannot be formed.

---

## 💻 Sample Input 

```php
Enter coin denominations separated by space:
1 2 5
Enter target amount:
11
```

---

## 💻 Expected Output 

```php
Minimum number of coins required: 3
```
