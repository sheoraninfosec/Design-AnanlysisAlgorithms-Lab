# N-Queens Problem – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **N-Queens Problem** using the **Backtracking technique**. The objective is to place **N queens on an N × N chessboard** such that no two queens attack each other.

A queen can attack horizontally, vertically, and diagonally, so the placement must ensure that no two queens share the same row, column, or diagonal.

This improved implementation prints **all possible solutions** and also displays the **total number of valid solutions**. For example, the classic **N = 8** problem has **92 valid solutions**.

---

## 🧠 Algorithm

1. Represent the board using a one-dimensional array where `board[row] = column`.
2. Start placing queens row by row.
3. For each column in the current row:
   - Check if placing the queen is safe:
     - No queen in the same column.
     - No queen on the same diagonal.
4. If the position is safe:
   - Place the queen and recursively move to the next row.
5. If all queens are placed successfully:
   - Store the solution.
6. After exploring all possibilities, print all solutions and the total count.

This approach uses **backtracking** to explore and prune invalid placements efficiently.

---

## 💻 Sample Input

```php
Enter value of N:
4
```

---

## 💻 Sample Output

```php
Total Solutions for N = 4: 2

Solution 1:
. Q . .
. . . Q
Q . . .
. . Q .

Solution 2:
. . Q .
Q . . .
. . . Q
. Q . .
```
