# Naive Matrix Multiplication – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Naive Matrix Multiplication algorithm** using the traditional triple nested loop method.

Matrix multiplication is performed only when the number of columns in Matrix A equals the number of rows in Matrix B.
This method directly follows the mathematical definition of matrix multiplication.

---

## 🧠 Algorithm Concept

For matrices A (n × m) and B (m × q):

C [i][j]  = Σ ( A [i][k] × B [k][j] )  
for k = 0 to m-1

The algorithm:
1. Initialize result matrix with zeros.
2. Use three nested loops.
3. Multiply corresponding elements and accumulate sum.

---

## ⏱ Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | O(n³) |
| Average Case | O(n³) |
| Worst Case | O(n³) |

Where n represents matrix dimension (for square matrices).

---

## 💻 Sample Input 

```php
Enter number of rows in Matrix A:
2
Enter number of columns in Matrix A:
2
Enter Matrix A row by row:
1 2
3 4
Enter number of rows in Matrix B:
2
Enter number of columns in Matrix B:
2
Enter Matrix B row by row:
5 6
7 8
```

---

## 💻 Sample Output 

```php
Resultant Matrix:
[19, 22]
[43, 50]
```
