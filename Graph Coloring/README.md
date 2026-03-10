# Graph Coloring – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Graph Coloring Problem** using the **Backtracking technique**.

The goal is to assign colors to vertices of a graph such that **no two adjacent vertices share the same color**. The number of colors available is limited to **k colors**.
Graph coloring is an **NP-hard problem** in general, but for small graphs it can be solved efficiently using backtracking.

This problem has applications in **register allocation, scheduling, and frequency assignment**.

---

## 🧠 Algorithm

1. Represent the graph using an **adjacency matrix**.
2. Start with the first vertex.
3. Try assigning one of the available colors (1 to k).
4. Check if assigning the color violates the constraint:
   - Adjacent vertices must not have the same color.
5. If safe:
   - Assign the color and move to the next vertex.
6. If no color is valid:
   - Backtrack and try another color for the previous vertex.
7. Continue until all vertices are successfully colored.

---

## 💻 Sample Input

```php
Enter number of vertices:
4

Enter adjacency matrix:
0 1 1 1
1 0 1 0
1 1 0 1
1 0 1 0

Enter number of colors:
3
```

---

💻 Sample Output

```php
Color assignment for vertices:
Vertex 0 → Color 1
Vertex 1 → Color 2
Vertex 2 → Color 3
Vertex 3 → Color 2
```
