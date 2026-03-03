# Rod Cutting Problem – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Rod Cutting Problem** using **Dynamic Programming**.

The objective is to determine the maximum profit obtainable by cutting a rod of length n into smaller pieces, given the prices of different lengths.
The rod can be cut into multiple pieces, and the goal is to maximize total revenue.

---

## 🧠 Algorithm Concept

Let:

dp[i] = Maximum obtainable profit for rod length i

Recurrence Relation:

dp[i] = max(price[j] + dp[i-j-1])

for j = 0 to i-1

The final answer is stored in:

dp[n]

---

## 💻 Sample Input 

```php
Enter length of rod:
8
Enter prices for each length from 1 to n:
1 5 8 9 10 17 17 20
```

---

## 💻 Expected Output

```php
Maximum Obtainable Profit: 22
```
