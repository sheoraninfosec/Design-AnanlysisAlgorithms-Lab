# Boyer-Moore Algorithm – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Boyer-Moore Algorithm**, one of the fastest string matching algorithms in practice.
It improves efficiency by skipping sections of the text using heuristics.

---

## 🧠 Algorithm Concept

Boyer-Moore compares the pattern from **right to left** and uses heuristics to skip unnecessary comparisons.

### Key Heuristic Used:
- **Bad Character Heuristic**:
  - When mismatch occurs, shift the pattern so that the mismatched character aligns with its last occurrence in the pattern.

### Steps:
1. Start comparison from the end of the pattern.
2. On mismatch, use bad character rule to shift pattern.
3. If match found, record index and shift.

---

## 💻 Sample Input 

```php
Enter text:
ABAAABCD

Enter pattern:
ABC
```

---

## 💻 Sample Output

```php
Pattern found at indices: [4]
```
