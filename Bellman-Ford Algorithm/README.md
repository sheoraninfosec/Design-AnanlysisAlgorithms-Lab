# Bellman-Ford Algorithm – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Bellman-Ford Algorithm** to compute the shortest paths from a single source vertex to all other vertices in a weighted directed graph.
Unlike Dijkstra’s algorithm, Bellman-Ford works correctly even when the graph contains **negative edge weights**. It can also detect the presence of **negative weight cycles**.

---

## 🧠 Algorithm Concept

The algorithm works as follows:

1. Initialize distances from source to all vertices as infinity.
2. Relax all edges (V-1) times.
3. Check for negative weight cycles:
   - If further relaxation is possible, a negative cycle exists.

Relaxation step:

if distance[u] + weight < distance[v]:
    distance[v] = distance[u] + weight

---

## ⏱ Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | O(VE) |
| Average Case | O(VE) |
| Worst Case | O(VE) |

Where V = number of vertices, E = number of edges.

---

## 💻 Sample Input 

```php
Enter vertices separated by space:
A B C D
Enter number of directed edges:
5
Enter edges in format: u v weight
A B 4
A C 5
B C -3
C D 4
B D 5
Enter source vertex:
A
```
