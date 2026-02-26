# Naive String Matching – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Naive String Matching algorithm** to find occurrences of a pattern within a given text.

The algorithm checks for a match by comparing the pattern with every possible substring of the text.
Although simple and easy to implement, it is not efficient for large inputs.

---

## 🧠 Algorithm Concept

The algorithm works as follows:

1. Let text length = n and pattern length = m.
2. Compare pattern with text from index 0 to n-m.
3. For each position:
   - Compare characters one by one.
   - If all characters match → record position.
4. Continue until all possible positions are checked.

---

## ⏱ Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | O(n) |
| Average Case | O(nm) |
| Worst Case | O(nm) |

Where:
- n = length of text
- m = length of pattern

---

## 💻 Sample Input 

```php
Enter the text string:
ABABDABACDABABCABAB
Enter the pattern to search:
ABABC
```

---

## 💻 Sample Output

```php
Pattern found at positions: [10]
```
