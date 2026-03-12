# Permutations & Combinations Generator – <br>  Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements a **Permutations and Combinations Generator** using the **Backtracking technique**.

Permutations generate all possible arrangements of elements in a set, while combinations generate all possible subsets of the set.
Permutation generation has a complexity of **O(n!)**, while combination generation explores **2ⁿ subsets**.

These techniques are widely used in **combinatorics, puzzle solving, optimization problems, and interview questions**.

---

## 🧠 Algorithm

Permutation Generation:
1. Fix an element at the current position.
2. Swap it with every other element that follows.
3. Recursively generate permutations for the remaining elements.
4. Backtrack by swapping elements back.

Combination Generation:
1. For each element, choose either:
   - Include the element in the subset.
   - Exclude the element.
2. Recursively explore both choices.
3. When all elements are processed, output the subset.

---

## 💻 Sample Input

```php
Enter elements separated by space:
A B C
```

---

## 💻 Sample Output

```php
Permutations:
['A', 'B', 'C']
['A', 'C', 'B']
['B', 'A', 'C']
['B', 'C', 'A']
['C', 'B', 'A']
['C', 'A', 'B']

Combinations:
['A', 'B', 'C']
['A', 'B']
['A', 'C']
['A']
['B', 'C']
['B']
['C']
[]
```
