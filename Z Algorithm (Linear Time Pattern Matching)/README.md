# Z Algorithm – <br>  Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Z Algorithm** for efficient pattern matching in linear time.
It computes a Z-array that helps identify pattern occurrences without redundant comparisons.

---

## 🧠 Algorithm Concept

The Z Algorithm constructs a **Z-array**, where:

- Z[i] = length of the longest substring starting from index i that matches the prefix of the string.

### Steps:
1. Concatenate: Pattern + "$" + Text
2. Compute Z-array for the combined string.
3. If Z[i] equals pattern length → pattern found.

---

## 💻 Sample Input 

```php
Enter text:
AABAACAADAABAABA

Enter pattern:
AABA
```

---

## 💻 Sample Output

```php
Pattern found at indices: [0, 9, 12]
```
