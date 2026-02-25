# Hash Table Search – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements **Hash Table Search** using the technique of **separate chaining** to handle collisions.

A hash table stores elements using a hash function that maps keys to specific indices. If multiple keys map to the same index, chaining is used to store them in a list at that index.
This allows efficient search operations.

---

## 🧠 Algorithm Concept

1. A hash function computes index:
   
   index = key % table_size

2. During insertion:
   - The key is stored at the computed index.
   - If collision occurs, it is added to the chain (list).

3. During search:
   - Compute index using hash function.
   - Search within the list at that index.

---

## ⏱ Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | O(1) |
| Average Case | O(1) |
| Worst Case | O(n) |

Worst case occurs when all elements hash to the same index.

---

## 💻 Sample Input 

```php
Enter size of hash table:
10
Enter number of elements to insert:
5
Enter elements:
15
25
35
20
30
Enter element to search:
25
```
