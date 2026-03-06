# Activity Selection Problem – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Activity Selection Problem** using a **Greedy Algorithm**.

The goal is to select the maximum number of activities that do not overlap, given their start and finish times.
The greedy strategy chooses the activity that finishes earliest.

---

## 🧠 Algorithm Concept

Steps of the algorithm:

1. Sort activities based on increasing finish time.
2. Select the first activity.
3. For each next activity:
   - If its start time ≥ finish time of last selected activity → select it.
4. Continue until all activities are checked.

This greedy strategy ensures maximum number of non-overlapping activities.

---

## 💻 Sample Input 

```php
Enter number of activities:
6
Enter start times separated by space:
1 3 0 5 8 5
Enter finish times separated by space:
2 4 6 7 9 9
```

---

## 💻 Expected Output

```php
Selected Activities (start, finish):
(1, 2)
(3, 4)
(5, 7)
(8, 9)
```
