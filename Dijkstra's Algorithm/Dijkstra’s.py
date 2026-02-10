# Author: Jigesh Sheoran
# Last Modified: 07/02/2026

import heapq
from collections import defaultdict

def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist > distance[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distance


# user input
n = int(input("Enter number of vertices: "))
graph = defaultdict(list)

print("Enter vertex names:")
vertices = [input() for _ in range(n)]

e = int(input("Enter number of weighted edges: "))
print("Enter edges (u v weight):")
for _ in range(e):
    u, v, w = input().split()
    graph[u].append((v, int(w)))
    graph[v].append((u, int(w)))

start = input("Enter source vertex: ")

distances = dijkstra(graph, start)
print("\nShortest distances using Dijkstra:")
for node, dist in distances.items():
    print(start, "→", node, "=", dist)
