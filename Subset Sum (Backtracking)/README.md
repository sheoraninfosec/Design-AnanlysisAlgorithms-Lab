# Subset Sum Problem – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Subset Sum Problem** using the **Backtracking technique**.

The objective is to find all subsets of a given set whose elements add up to a specified **target sum**.

Instead of checking every possible subset blindly (which would take O(2ⁿ) time), backtracking **prunes invalid paths early**, making the algorithm significantly more efficient in practice.

---

## 🧠 Algorithm

1. Start with an empty subset.
2. Recursively explore two possibilities for each element:
   - Include the element in the subset.
   - Exclude the element from the subset.
3. If the subset sum equals the target:
   - Store the subset as a valid solution.
4. If the sum exceeds the target or all elements are processed:
   - Backtrack and try another combination.
5. Continue until all possible valid subsets are explored.

---

## 💻 Sample Input

```php
Enter set elements separated by space:
2 4 6 10
Enter target sum:
16
```

---

💻 Sample Output

```php
Subsets with the given sum:
[6, 10]
[2, 4, 10]
```
