# Author: Jigesh Sheoran
# Last Modified : 13 / 03 / 2026
# Experiment: Edmonds-Karp Algorithm (Maximum Flow)

from collections import deque

def bfs(capacity, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()

        for v in capacity[u]:
            if v not in visited and capacity[u][v] > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True

    return False


def edmonds_karp(capacity, source, sink):
    parent = {}
    max_flow = 0

    while bfs(capacity, source, sink, parent):
        path_flow = float('inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v].setdefault(u, 0)
            capacity[v][u] += path_flow
            v = parent[v]

    return max_flow

# user input
print("Edmonds-Karp Algorithm (Maximum Flow)")

vertices = input("Enter vertices separated by space:\n").split()

capacity = {v: {} for v in vertices}

e = int(input("Enter number of edges:\n"))

print("Enter edges in format: u v capacity")

for i in range(e):
    u, v, w = input(f"Edge {i+1}: ").split()
    capacity[u][v] = int(w)
    if v not in capacity:
        capacity[v] = {}

source = input("Enter source vertex:\n")
sink = input("Enter sink vertex:\n")

max_flow = edmonds_karp(capacity, source, sink)

print("\nMaximum Flow:", max_flow)
