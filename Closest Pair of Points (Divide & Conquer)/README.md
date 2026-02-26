# Closest Pair of Points – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Closest Pair of Points algorithm** using the Divide and Conquer approach.

The goal is to find the minimum distance between any two points in a 2D plane.
The divide-and-conquer method improves performance significantly compared to the brute-force approach.

---

## 🧠 Algorithm Concept

The algorithm works as follows:

1. Sort points based on x-coordinate.
2. Divide the points into two halves.
3. Recursively find the closest pair in left and right halves.
4. Compute minimum of both halves.
5. Check the strip area near the dividing line for possible closer pairs.

Distance Formula:

d = √((x₂ - x₁)² + (y₂ - y₁)²)

---

## ⏱ Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |

Brute-force approach takes O(n²).

---

## 💻 Sample Input 

```php
Enter number of points:
4
Enter points as x y:
2 3
12 30
40 50
5 1
```
