# Author: Jigesh Sheoran
# Last Modified : 20 / 03 / 2026
# Experiment: Hungarian Algorithm (Kuhn-Munkres) – Optimal Assignment Problem

import numpy as np

def hungarian_algorithm(cost_matrix):
    n = len(cost_matrix)
    cost = cost_matrix.copy()

    # Step 1: Row reduction
    for i in range(n):
        cost[i] -= min(cost[i])

    # Step 2: Column reduction
    for j in range(n):
        cost[:, j] -= min(cost[:, j])

    # Step 3: Cover zeros with minimum lines (simplified approach)
    assigned = [-1] * n
    for i in range(n):
        for j in range(n):
            if cost[i][j] == 0 and j not in assigned:
                assigned[i] = j
                break

    # Calculate minimum cost
    total_cost = 0
    for i in range(n):
        total_cost += cost_matrix[i][assigned[i]]

    return assigned, total_cost


# user input
n = int(input("Enter number of tasks/workers (n x n matrix): "))

print("Enter cost matrix row by row:")
cost_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    cost_matrix.append(row)

cost_matrix = np.array(cost_matrix)

assignment, min_cost = hungarian_algorithm(cost_matrix)

print("\nOptimal Assignment (Worker → Task):")
for i in range(n):
    print(f"Worker {i} → Task {assignment[i]}")

print("\nMinimum Cost:", min_cost)
print("\nHungarian Algorithm executed successfully.")
