# Counting Sort – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Counting Sort algorithm**, a **non-comparison-based sorting technique** used for sorting integers within a known range.

Instead of comparing elements, the algorithm counts the number of occurrences of each value and uses this information to determine their correct position in the sorted array.
Counting Sort is efficient when the range of input values is not significantly larger than the number of elements.

---

## 🧠 Algorithm

1. Find the **maximum element** in the array.
2. Create a **count array** to store the frequency of each element.
3. Compute the **cumulative sum** of the count array.
4. Place elements into the output array using the cumulative count values.
5. Copy the sorted elements back to the original array or output the sorted array.

---

## 💻 Sample Input

```php
Enter non-negative integers separated by space:
4 2 2 8 3 3 1
```

---

## 💻 Sample Output

```php
Sorted Array:
[1, 2, 2, 3, 3, 4, 8]
```
