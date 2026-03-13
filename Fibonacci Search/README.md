# Fibonacci Search – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Fibonacci Search algorithm**, a searching technique used on **sorted arrays**.

Instead of dividing the search space in half like binary search, Fibonacci search divides the array using **Fibonacci numbers** to determine probe positions.
It is useful in scenarios where **division operations are costly**, such as older storage systems like magnetic tapes.

The algorithm repeatedly reduces the search range using Fibonacci numbers until the element is found or the range becomes empty.

---

## 🧠 Algorithm

1. Generate Fibonacci numbers until a Fibonacci number is greater than or equal to the array size.
2. Use Fibonacci numbers to divide the array into sections.
3. Compare the target element with the element at the calculated index.
4. If the element is smaller, move the search range to the left portion.
5. If the element is larger, move the search range to the right portion.
6. Continue reducing the Fibonacci range until the element is found or the search range becomes empty.

---

## 💻 Sample Input

```php
Enter sorted elements separated by space:
10 22 35 40 45 50 80 82 85 90
Enter element to search:
85
```

---

## 💻 Sample Output

```php
Element found at index 8
```
