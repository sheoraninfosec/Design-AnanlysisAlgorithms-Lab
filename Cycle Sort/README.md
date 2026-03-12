# Cycle Sort – <br>Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Cycle Sort algorithm**, an in-place sorting technique designed to minimize the number of memory writes.

Cycle Sort works by placing each element directly into its correct position by rotating elements in cycles. 
It is particularly useful in situations where **write operations are expensive**, such as flash memory systems.
The algorithm minimizes writes by ensuring each value is written only once to its correct location.

---

## 🧠 Algorithm

1. Start from the first element and determine its correct position in the array.
2. Count the number of elements smaller than the current element to determine the correct index.
3. Swap the element into its correct position.
4. If the swapped element is not in the correct position, repeat the process to complete the cycle.
5. Continue until all cycles are completed and the array is sorted.

---

## 💻 Sample Input

```php
Enter elements separated by space:
20 40 50 10 30
```

---

## 💻 Sample Output

```php
Sorted Array:
[10, 20, 30, 40, 50]
```
