# Borůvka's Algorithm – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements **Borůvka's Algorithm**, one of the earliest algorithms for computing a **Minimum Spanning Tree (MST)** in a weighted graph.

First introduced in **1926**, Borůvka's algorithm repeatedly finds the **cheapest edge connecting each component** and merges those components. 
The process continues until only one component remains, forming the MST.
The algorithm is particularly useful in **parallel and distributed computing** because multiple components can select their cheapest edges simultaneously.

The time complexity is **O(E log V)**.

---

## 🧠 Algorithm

1. Start with each vertex as an individual component.
2. For each component, find the **minimum-weight outgoing edge**.
3. Add all such edges to the MST simultaneously.
4. Merge the connected components using union-find.
5. Repeat until only one component remains.
6. The selected edges form the **Minimum Spanning Tree**.

---

## 💻 Sample Input

```php
Enter number of vertices:
4
Enter number of edges:
5

Enter edges in format: u v weight
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4
```

---

## 💻 Sample Output

```php
Minimum Spanning Tree:
Edge 2 - 3 with weight 4 included in MST
Edge 0 - 3 with weight 5 included in MST
Edge 0 - 1 with weight 10 included in MST
Total MST weight: 19
```
