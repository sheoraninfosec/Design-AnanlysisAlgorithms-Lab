# Hungarian Algorithm (Kuhn-Munkres) – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Hungarian Algorithm (Kuhn-Munkres Algorithm)** to solve the **Assignment Problem**.

The goal is to assign tasks to workers such that the total cost is minimized, with each worker assigned exactly one task.

---

## 🧠 Algorithm Concept

The Hungarian Algorithm works in the following steps:

1. Perform **row reduction** (subtract minimum element of each row).
2. Perform **column reduction** (subtract minimum element of each column).
3. Cover all zeros using minimum number of lines.
4. Adjust the matrix if optimal assignment is not possible.
5. Repeat until an optimal assignment is found.

---

## ⚙️ Complexity

- Time Complexity: **O(n³)**
- Space Complexity: **O(n²)**

---

## 💻 Sample Input 

```php
Enter number of tasks/workers (n x n matrix):
3
Enter cost matrix row by row:
4 1 3
2 0 5
3 2 2
```

---

## 💻 Sample Output

```php
Optimal Assignment (Worker → Task):
Worker 0 → Task 1
Worker 1 → Task 0
Worker 2 → Task 2

Minimum Cost: 5
```
