# A* Algorithm – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **A* (A-Star) Search Algorithm** to find the shortest path between a start node and a goal node.
A* is an informed search algorithm that combines the advantages of Dijkstra’s Algorithm and Greedy Best-First Search. It uses a heuristic function to guide the search efficiently toward the goal.

---

## 🧠 Algorithm Concept

A* uses the evaluation function:

f(n) = g(n) + h(n)

Where:
- g(n) → Actual cost from start node to current node
- h(n) → Heuristic estimate from current node to goal
- f(n) → Estimated total cost

The algorithm:
1. Initialize start node.
2. Expand node with lowest f(n).
3. Update neighbors using cost formula.
4. Repeat until goal is reached.

---

## ⏱ Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | O(E) |
| Average Case | O(E log V) |
| Worst Case | O(V²) |

Performance depends on the heuristic used.

---

## 💻 Sample Input 

```php
Enter vertices separated by space:
A B C D E
Enter number of edges:
6
Enter edges in format: u v weight
A B 1
A C 3
B D 2
C D 1
D E 5
C E 4
Enter heuristic values for each vertex:
h(A) = 7
h(B) = 6
h(C) = 2
h(D) = 1
h(E) = 0
Enter start node:
A
Enter goal node:
E
```
