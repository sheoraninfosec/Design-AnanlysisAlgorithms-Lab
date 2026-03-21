# KMP (Knuth-Morris-Pratt) Algorithm – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **KMP (Knuth-Morris-Pratt) Algorithm** for efficient string pattern matching.
Unlike naive string matching, KMP avoids unnecessary comparisons by using information from previous matches.

---

## 🧠 Algorithm Concept

KMP uses a preprocessing step to build an array called:

- **LPS (Longest Prefix Suffix)**

This array stores the length of the longest prefix which is also a suffix.

### Steps:
1. Preprocess the pattern to create LPS array.
2. Compare pattern with text.
3. On mismatch, use LPS to skip comparisons.
4. Continue until full pattern is matched.

---

## 💻 Sample Input 

```php
Enter text:
ABABDABACDABABCABAB

Enter pattern:
ABABCABAB
```

---

## 💻 Sample Output

```php
Pattern found at indices: [10]
```
