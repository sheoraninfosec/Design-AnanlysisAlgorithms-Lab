# Edmonds-Karp Algorithm – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Edmonds-Karp Algorithm**, a specific implementation of the **Ford-Fulkerson method** used to compute the **maximum flow in a flow network**.

The algorithm repeatedly finds the **shortest augmenting path** from the source to the sink using **Breadth-First Search (BFS)**. 
Each augmenting path increases the flow until no more paths exist.
Because BFS is used to find augmenting paths, Edmonds-Karp guarantees a polynomial time complexity of **O(VE²)**.

---

## 🧠 Algorithm

1. Represent the flow network using a **capacity graph**.
2. Perform **Breadth-First Search (BFS)** to find the shortest augmenting path from source to sink.
3. Determine the **minimum residual capacity** along the path.
4. Update the residual capacities of edges along the path.
5. Add the path flow to the total flow.
6. Repeat until no augmenting path exists between source and sink.

---

## 💻 Sample Input

```php
Enter vertices separated by space:
S A B C T

Enter number of edges:
6

Enter edges in format: u v capacity
S A 10
S B 5
A B 15
A C 10
B C 10
C T 10

Enter source vertex:
S
Enter sink vertex:
T
```

---

## 💻 Sample Output

```php
Maximum Flow: 15
```
