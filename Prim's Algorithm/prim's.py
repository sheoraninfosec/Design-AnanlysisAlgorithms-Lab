# Author: Jigesh Sheoran
# Last Modified: 10/02/2026

import heapq
from collections import defaultdict

def prim(graph, start):
    visited = set()
    pq = [(0, start)]
    total_cost = 0

    while pq:
        cost, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        total_cost += cost

        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                heapq.heappush(pq, (weight, neighbour))

    return total_cost


# user input
graph = defaultdict(list)

n = int(input("Enter number of vertices: "))
vertices = []

print("Enter vertex names:")
for i in range(n):
    vertices.append(input(f"Vertex {i+1}: "))

e = int(input("Enter number of edges: "))
print("Enter edges in format: u v weight")

for i in range(e):
    u, v, w = input(f"Edge {i+1}: ").split()
    w = int(w)
    graph[u].append((v, w))
    graph[v].append((u, w))   # undirected graph

start = input("Enter starting vertex: ")
mst_cost = prim(graph, start)

print("\nMinimum Spanning Tree Cost:", mst_cost)
print("Prim's Algorithm executed successfully.")
