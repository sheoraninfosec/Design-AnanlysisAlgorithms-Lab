# Author: Jigesh Sheoran
# Last Modified: 07/02/2026

from collections import deque, defaultdict

def bfs_shortest_path(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distance[neighbor] == float('inf'):
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return distance


# user input
n = int(input("Enter number of vertices: "))
graph = defaultdict(list)

print("Enter vertex names:")
vertices = [input() for _ in range(n)]

e = int(input("Enter number of edges: "))
print("Enter edges (u v):")
for _ in range(e):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)

start = input("Enter source vertex: ")

distances = bfs_shortest_path(graph, start)
print("\nShortest distances using BFS:")
for node, dist in distances.items():
    print(start, "→", node, "=", dist)
