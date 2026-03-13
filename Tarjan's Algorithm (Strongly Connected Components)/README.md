# Tarjan's Algorithm – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements **Tarjan's Algorithm** to find **Strongly Connected Components (SCCs)** in a directed graph.

Tarjan's algorithm performs the task in a **single Depth First Search (DFS) traversal**, making it highly efficient with a time complexity of **O(V + E)**.
The algorithm uses a stack and a concept called **low-link values** to identify components where every vertex is reachable from every other vertex in the same component.

It is widely used in graph analysis and can also be adapted to find **articulation points, bridges, and biconnected components**.

---

## 🧠 Algorithm

1. Perform a **Depth First Search (DFS)** on the graph.
2. Assign each node a unique discovery index.
3. Maintain a stack to track nodes currently in the DFS path.
4. Compute **low-link values**, which represent the smallest reachable index.
5. When a node's index equals its low-link value, it forms the root of an SCC.
6. Pop nodes from the stack until the root node is reached, forming a strongly connected component.

---

## 💻 Sample Input

```php
Enter vertices separated by space:
A B C D E

Enter number of directed edges:
6

Enter edges in format: u v
A B
B C
C A
B D
D E
E D
```

---

## 💻 Sample Output

```php
Strongly Connected Components:
['C', 'B', 'A']
['E', 'D']
```
