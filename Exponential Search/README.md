# Exponential Search – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Exponential Search algorithm** for searching an element in a sorted array.

Exponential Search first identifies a search range by repeatedly doubling the index. After finding the probable range, it applies **Binary Search** within that range.
It is particularly efficient for large sorted arrays and when the target element is near the beginning.

---

## 🧠 Algorithm Concept

The algorithm works in two phases:

1. If the first element matches the key, return immediately.
2. Find a range where the element may exist by doubling the index:
   
   i = 1  
   while i < n and arr[i] <= key:  
       i = i * 2  

3. Perform Binary Search in the range:

   low = i/2  
   high = min(i, n-1)

---

## ⏱ Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | O(1) |
| Average Case | O(log n) |
| Worst Case | O(log n) |

---

## 💻 Sample Input 

```php
Enter sorted elements separated by space:
10 20 30 40 50 60 70 80
Enter element to search:
50
```
