# Rabin-Karp Algorithm – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Rabin-Karp Algorithm**, a string matching algorithm that uses **hashing** to find patterns in text efficiently.
Instead of comparing characters directly, it compares hash values of substrings.

---

## 🧠 Algorithm Concept

The Rabin-Karp algorithm works as follows:

1. Compute hash value of the pattern.
2. Compute hash value of the first window of text.
3. Slide the window over text:
   - If hash matches → verify characters.
   - Else → update hash using rolling hash.
4. Repeat until the end of the text.

---

## 💻 Sample Input 

```php
Enter text:
GEEKSFORGEEKS

Enter pattern:
GEEK
```

---

## 💻 Sample Output

```php
Pattern found at indices: [0, 8]
```
