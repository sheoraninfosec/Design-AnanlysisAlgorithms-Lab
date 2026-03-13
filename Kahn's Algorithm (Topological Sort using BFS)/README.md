# Kahn's Algorithm – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements **Kahn's Algorithm** for performing **Topological Sorting** on a **Directed Acyclic Graph (DAG)**.

Kahn's algorithm uses a **Breadth-First Search (BFS)** approach based on **in-degree counts**. Vertices with zero in-degree are processed first, and their outgoing edges are removed from the graph.

If all vertices are processed successfully, the graph is a DAG. If some vertices remain unprocessed, the graph contains a **cycle**.
The time complexity of the algorithm is **O(V + E)**.

---

## 🧠 Algorithm

1. Compute the **in-degree** (number of incoming edges) for each vertex.
2. Add all vertices with **in-degree 0** to a queue.
3. Remove a vertex from the queue and add it to the topological order.
4. Reduce the in-degree of its adjacent vertices by 1.
5. If any adjacent vertex becomes **0 in-degree**, add it to the queue.
6. Repeat until the queue becomes empty.
7. If all vertices are processed, the topological order is valid.
8. If some vertices remain, the graph contains a **cycle**.

---

## 💻 Sample Input

```php
Enter vertices separated by space:
A B C D E F

Enter number of directed edges:
6

Enter edges in format: u v
A C
B C
B D
C E
D F
E F
```

---

## 💻 Sample Output

```php
Topological Order: ['A', 'B', 'C', 'D', 'E', 'F']
```
