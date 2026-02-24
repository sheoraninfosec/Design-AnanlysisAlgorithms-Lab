# 🔢 Selection Sort Algorithm

## 📘 Theory

Selection Sort is a simple comparison-based sorting algorithm.  
It repeatedly selects the smallest element from the unsorted portion of the list and places it at the beginning.

The list is divided into two parts:
- Sorted portion
- Unsorted portion

After each pass, one element is placed in its correct position.

### ⏱ Time Complexity

- Best Case: O(n²)
- Worst Case: O(n²)
- Space Complexity: O(1)

---

## 🧠 Algorithm

1. Start from the first element of the list.
2. Assume the current position contains the minimum value.
3. Compare it with the remaining unsorted elements.
4. Find the smallest element in the unsorted part.
5. Swap it with the current position.
6. Move to the next position.
7. Repeat until the entire list is sorted.

---

## 🧪 Sample Input

```
Enter number of elements:
6

Enter elements:
64 25 12 22 11 90
```

---

## ✅ Sample Output

```
Sorted List:
[11, 12, 22, 25, 64, 90]
```
