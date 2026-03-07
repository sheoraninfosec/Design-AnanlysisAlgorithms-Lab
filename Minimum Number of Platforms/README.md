# Minimum Number of Platforms <br> – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Minimum Number of Platforms problem**.

The objective is to determine the minimum number of railway platforms required so that no train has to wait.
The approach sorts arrival and departure times and uses a **two-pointer sweep technique** to track overlapping trains.

---

## 🧠 Algorithm Concept

Steps of the algorithm:

1. Sort arrival times.
2. Sort departure times.
3. Use two pointers:
   - One for arrivals
   - One for departures
4. If arrival time ≤ departure time:
   - Increase platform count.
5. Otherwise:
   - Decrease platform count.
6. Track the maximum number of platforms needed.

---

## 💻 Sample Input 

```php
Enter arrival times separated by space:
900 940 950 1100 1500 1800
Enter departure times separated by space:
910 1200 1120 1130 1900 2000
```

---

## Expected Output

```php
Minimum number of platforms required: 3
```
