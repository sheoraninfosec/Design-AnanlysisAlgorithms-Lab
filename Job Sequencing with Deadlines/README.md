# Job Sequencing with Deadlines – Design and Analysis of Algorithms Lab

---

## 📌 Overview

This experiment implements the **Job Sequencing with Deadlines problem** using a **Greedy Algorithm**.

Each job has a deadline and profit. The objective is to schedule jobs within their deadlines to maximize total profit.
Each job takes one unit of time and only one job can be executed at a time.

---

## 🧠 Algorithm Concept

Steps of the algorithm:

1. Sort jobs in descending order of profit.
2. Create time slots up to the maximum deadline.
3. For each job:
   - Find the latest available slot before its deadline.
   - Assign the job to that slot.
4. Continue until all jobs are processed.

This greedy strategy maximizes profit while respecting deadlines.

---

## 💻 Sample Input 

```php
Enter number of jobs:
5
Enter jobs in format: job_id deadline profit
J1 2 100
J2 1 19
J3 2 27
J4 1 25
J5 3 15
```

---

## 💻 Expected Output

```php
Scheduled Jobs: ['J1', 'J3', 'J5']
Maximum Profit: 142
```
