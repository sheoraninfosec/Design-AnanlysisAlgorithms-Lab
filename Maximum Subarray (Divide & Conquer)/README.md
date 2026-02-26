# Maximum Subarray (Divide & Conquer) – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Maximum Subarray Problem** using the Divide and Conquer approach.

The goal is to find the contiguous subarray within a one-dimensional array that has the largest sum.
The divide-and-conquer method splits the array into two halves and computes the maximum subarray in left, right, and crossing regions.

---

## 🧠 Algorithm Concept

The algorithm works as follows:

1. Divide the array into two halves.
2. Recursively find:
   - Maximum subarray in left half.
   - Maximum subarray in right half.
3. Compute maximum crossing sum.
4. Return the maximum of the three.

Crossing sum includes elements from both halves.

---

## ⏱ Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |

Divide and Conquer recurrence:

T(n) = 2T(n/2) + O(n)

---

## 💻 Sample Input 

```php
Enter array elements separated by space:
-2 -5 6 -2 -3 1 5 -6
```
