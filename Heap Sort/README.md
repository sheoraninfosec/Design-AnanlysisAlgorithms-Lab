# 🌲 Heap Sort Algorithm

## 🎯 Objective

Implemening the **Heap Sort algorithm** to sort a list of elements in ascending order.

---

## 📘 Theory

Heap Sort is a comparison-based sorting algorithm that uses a **Binary Heap data structure**.

It works in two main steps:

1. Build a **Max Heap** from the input data.
2. Repeatedly extract the maximum element from the heap and place it at the end of the list.

A Max Heap is a complete binary tree where:
- The parent node is greater than or equal to its children.

### ⏱ Time Complexity

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)
- Space Complexity: O(1)

---

## 🧠 Algorithm

1. Build a Max Heap from the given list.
2. Swap the root (maximum element) with the last element.
3. Reduce heap size by one.
4. Heapify the root again.
5. Repeat until the heap size becomes 1.

---

## 🧪 Sample Input

```php
Enter number of elements:
7

Enter elements:
12 11 13 5 6 7 20
```

---

## ✅ Sample Output

```
Sorted List:
[5, 6, 7, 11, 12, 13, 20]
```
