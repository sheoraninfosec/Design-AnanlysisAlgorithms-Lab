# Shell Sort – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Shell Sort algorithm**, an improvement over the traditional **Insertion Sort**.

Shell Sort works by comparing elements that are far apart using a **gap sequence**, gradually reducing the gap until it becomes 1. When the gap is 1, the algorithm performs a final insertion sort pass.

By allowing exchanges of distant elements, Shell Sort significantly improves performance compared to standard insertion sort for large arrays.

---

## 🧠 Algorithm

1. Start with a large gap value (usually n/2).
2. Divide the array into sublists based on the gap.
3. Perform insertion sort on elements separated by the gap.
4. Reduce the gap (typically gap = gap / 2).
5. Repeat the process until the gap becomes 1.
6. The final pass produces a fully sorted array.

---

## 💻 Sample Input

```php
Enter elements separated by space:
23 12 1 8 34 54 2 3
```

---

## 💻 Sample Output

```php
Sorted Array:
[1, 2, 3, 8, 12, 23, 34, 54]
```
