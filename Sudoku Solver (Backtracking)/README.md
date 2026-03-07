# Sudoku Solver – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements a **Sudoku Solver** using the **Backtracking algorithm**.

The goal is to fill a **9 × 9 Sudoku grid** so that:

- Each row contains digits **1–9 without repetition**
- Each column contains digits **1–9 without repetition**
- Each **3 × 3 subgrid** contains digits **1–9 without repetition**

The solver systematically tries numbers and uses **backtracking** to undo incorrect choices until a valid solution is found.

---

## 🧠 Algorithm

1. Scan the grid to find an empty cell (represented by `0`).
2. Try placing numbers **1–9** in the empty cell.
3. Check if the number satisfies:
   - Row constraint
   - Column constraint
   - 3 × 3 box constraint
4. If valid:
   - Place the number and recursively solve the remaining grid.
5. If the placement leads to a conflict:
   - Undo the move (backtrack) and try the next number.
6. Continue until the grid is completely filled.

---

## 💻 Sample Input

```php
Enter Sudoku grid (0 represents empty cell):

5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

---

## 💻 Sample Output

```php
Solved Sudoku:

5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```
