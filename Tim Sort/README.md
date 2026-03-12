# Tim Sort – <br> Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements **Tim Sort**, a hybrid sorting algorithm derived from **Merge Sort and Insertion Sort**.

Tim Sort is designed to perform efficiently on real-world data and is the default sorting algorithm used in **Python and Java**.
The algorithm divides the array into small segments called **runs**, sorts each run using insertion sort, and then merges them together using merge sort.

---

## 🧠 Algorithm

1. Divide the array into small segments called **runs**.
2. Sort each run using **Insertion Sort**.
3. Merge the sorted runs using **Merge Sort**.
4. Continue merging until the entire array becomes sorted.

Tim Sort takes advantage of partially sorted data, making it highly efficient in practice.

---

## 💻 Sample Input

```php
Enter elements separated by space:
9 3 7 1 8 2 6 5 4
```

---

## 💻 Sample Output

```php
Sorted Array:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
