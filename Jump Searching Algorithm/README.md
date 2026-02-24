# 🔎 Jump Search Algorithm

## 📘 Theory

Jump Search is an efficient searching algorithm for **sorted arrays**.

Instead of checking each element sequentially (like Linear Search), it:
1. Jumps ahead by fixed steps.
2. Once the possible block is identified, it performs linear search within that block.

The optimal jump size is √n.

Jump Search performs better than Linear Search but slower than Binary Search.

### ⏱ Time Complexity

- Best Case: O(1)
- Worst Case: O(√n)
- Space Complexity: O(1)

---

## 🧠 Algorithm

1. Compute step size = √n.
2. Jump ahead in blocks of size √n.
3. Stop when the block containing the key is found.
4. Perform linear search within that block.
5. If element is found, return its index.
6. Otherwise, return -1.

---

## 🧪 Sample Input

```php
Enter number of elements:
8

Enter sorted elements:
2 5 8 12 16 23 38 56

Enter element to search:
23
```

---

## ✅ Sample Output

```php
Element found at position: 6
```
