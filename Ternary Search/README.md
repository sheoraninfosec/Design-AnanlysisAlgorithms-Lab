# Ternary Search – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Ternary Search algorithm**, a divide-and-conquer searching technique used on **sorted arrays**.

Unlike binary search, which divides the search space into two parts, ternary search divides the array into **three parts** using two midpoints. It is commonly used in optimization problems, especially for finding the minimum or maximum of **unimodal functions**.

The time complexity of ternary search is **O(log₃ n)**.

---

## 🧠 Algorithm

1. Start with the entire sorted array.
2. Compute two midpoints:
   - mid₁ = left + (right − left) / 3
   - mid₂ = right − (right − left) / 3
3. Compare the key with elements at mid₁ and mid₂.
4. If the key matches either midpoint, return the index.
5. If the key is smaller than mid₁, search in the first third.
6. If the key is larger than mid₂, search in the last third.
7. Otherwise, search in the middle segment.
8. Repeat until the element is found or the search space becomes empty.

---

## 💻 Sample Input

```php
Enter sorted elements separated by space:
2 5 8 12 16 23 38 56 72
Enter element to search:
23
```

---

## 💻 Sample Output

```php
Element found at index 5
```
