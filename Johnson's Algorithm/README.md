# Johnson's Algorithm – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements **Johnson's Algorithm**, an efficient method for solving the **All-Pairs Shortest Path problem** in weighted graphs.

Johnson's Algorithm is particularly effective for **sparse graphs**, where it performs better than Floyd-Warshall. The algorithm first uses **Bellman-Ford** to reweight edges so that all edge weights become non-negative. After reweighting, **Dijkstra’s algorithm** is run from every vertex to compute the shortest paths.

The overall time complexity is **O(V² log V + VE)**.

---

## 🧠 Algorithm

1. Add a new temporary vertex connected to all vertices with weight 0.
2. Run **Bellman-Ford** from the new vertex to compute potential values for each vertex.
3. Use these values to **reweight edges**, ensuring all weights become non-negative.
4. Remove the temporary vertex.
5. Run **Dijkstra’s algorithm** from every vertex to compute shortest paths.
6. Adjust the final distances to obtain the original shortest path values.

---

## 💻 Sample Input

```php
Enter vertices separated by space:
A B C D

Enter number of edges:
5

Enter edges in format: u v weight
A B 4
A C 2
B C 5
B D 10
C D 3
```

---

## 💻 Sample Output

```php
All-Pairs Shortest Paths:
A: {'A': 0, 'B': 4, 'C': 2, 'D': 5}
B: {'A': inf, 'B': 0, 'C': 5, 'D': 8}
C: {'A': inf, 'B': inf, 'C': 0, 'D': 3}
D: {'A': inf, 'B': inf, 'C': inf, 'D': 0}
```
