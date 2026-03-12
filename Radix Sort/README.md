# Radix Sort – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Radix Sort algorithm**, a **non-comparison-based sorting technique** used for sorting integers digit by digit.

Radix Sort processes numbers starting from the **least significant digit (LSD)** to the **most significant digit (MSD)** using a stable sorting algorithm such as **Counting Sort**.

It is particularly efficient when sorting large numbers of integers with a fixed number of digits.

---

## 🧠 Algorithm

1. Find the **maximum number** in the array to determine the number of digits.
2. Starting from the **least significant digit**, perform counting sort on each digit position.
3. Move to the next digit by increasing the exponent (10, 100, 1000, etc.).
4. Repeat the process until all digit positions have been processed.
5. After processing all digits, the array becomes fully sorted.

---

## 💻 Sample Input

```php
Enter non-negative integers separated by space:
170 45 75 90 802 24 2 66
```

---

## 💻 Sample Output

```php
Sorted Array:
[2, 24, 45, 66, 75, 90, 170, 802]
```
