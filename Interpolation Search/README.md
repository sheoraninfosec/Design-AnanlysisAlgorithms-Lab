# Interpolation Search – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Interpolation Search algorithm** for searching an element in a sorted array.

Interpolation Search improves upon Binary Search by estimating the position of the search key based on value distribution rather than always checking the middle element.

It works best when elements are **uniformly distributed**.

---

## 🧠 Algorithm Concept

The estimated position is calculated using:

pos = low + ((key - arr[low]) * (high - low)) / (arr[high] - arr[low])

The algorithm:
1. Estimates probable position.
2. Compares key with estimated position.
3. Adjusts search range accordingly.
4. Repeats until element is found or range collapses.

---

## ⏱ Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | O(1) |
| Average Case | O(log log n) |
| Worst Case | O(n) |

---

## 💻 How to Run

```bash
python interpolation_search.py
