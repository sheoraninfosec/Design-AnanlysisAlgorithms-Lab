# Bucket Sort – <br>Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Bucket Sort algorithm**, a **distribution-based sorting technique** used for sorting numbers that are uniformly distributed over a specific range.

The algorithm divides the input elements into several buckets, sorts each bucket individually, and then concatenates all buckets to produce the final sorted array.
Bucket Sort performs efficiently when input values are **uniformly distributed**, making it useful in cases involving floating-point numbers.

---

## 🧠 Algorithm

1. Create **n empty buckets** for n elements.
2. Distribute each element into the appropriate bucket based on its value.
3. Sort each bucket individually (commonly using insertion sort or built-in sort).
4. Concatenate all buckets in order.
5. The resulting sequence forms the sorted array.

---

## 💻 Sample Input

```php
Enter decimal numbers between 0 and 1 separated by space:
0.42 0.32 0.23 0.52 0.25 0.47 0.51
```

---

## 💻 Sample Output

```php
Sorted Array:
[0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]
```
