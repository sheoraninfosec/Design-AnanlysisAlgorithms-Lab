# Rat in a Maze –<br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Rat in a Maze problem** using the **Backtracking technique**.

The objective is to find a path for a rat to travel from the **top-left corner to the bottom-right corner** of a maze. The rat can only move through **open cells (1)** and must avoid **blocked cells (0)**.
The algorithm explores possible paths and uses backtracking to undo moves that lead to dead ends until a valid path is found.

---

## 🧠 Algorithm

1. Start from the top-left cell `(0,0)`.
2. Check if the current cell is safe (within bounds and not blocked).
3. Mark the cell as part of the solution path.
4. Recursively try the next moves:
   - Move **Down**
   - Move **Right**
5. If both moves fail, **backtrack** by unmarking the cell.
6. Continue until the bottom-right cell is reached.

---

## 💻 Sample Input

```php
Enter size of maze (n for n×n):
4

Enter maze matrix (1 = open path, 0 = blocked):

1 0 0 0
1 1 0 1
0 1 0 0
1 1 1 1
```

---

## 💻 Sample Output

```php
Path for the rat:

1 0 0 0
1 1 0 0
0 1 0 0
0 1 1 1
```
