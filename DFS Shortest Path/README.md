# 🔍 DFS Based Shortest Path

## 🎯 Objective

To implement **Depth First Search (DFS)** to find the shortest path between two vertices in a graph.

---

## 🧠 Algorithm

1. Start from the source node.
2. Mark the current node as visited.
3. Add the current node to the path.
4. If the current node is the destination:
   - Compare the current path length with the minimum path found so far.
5. Recursively visit all unvisited neighboring vertices.
6. Backtrack by removing the node from the current path.
7. Repeat until all possible paths are explored.
8. Return the shortest path found.

---

## 💻 Sample Input

```python
Enter vertices separated by space:
A B C D E F

Enter number of edges:
6

Enter edges:
A B
A C
B D
C D
D E
E F

Enter source vertex:
A

Enter destination vertex:
F
