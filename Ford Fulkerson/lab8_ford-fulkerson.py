# Author: Jigesh Sheoran
# Last Modified: 17/02/2026

from collections import deque, defaultdict

def bfs(residual, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()

        for v in residual[u]:
            if v not in visited and residual[u][v] > 0:
                visited.add(v)
                parent[v] = u
                queue.append(v)
    return sink in visited

def ford_fulkerson(graph, source, sink):
    residual = defaultdict(dict)

    # Initialize residual graph
    for u in graph:
        for v in graph[u]:
            residual[u][v] = graph[u][v]
            if u not in residual[v]:
                residual[v][u] = 0
    parent = {}
    max_flow = 0

    while bfs(residual, source, sink, parent):
        path_flow = float('inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, residual[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = parent[v]
    return max_flow


# user input
graph = defaultdict(dict)

vertices = input("Enter vertices separated by space: ").split()

e = int(input("Enter number of directed edges: "))
print("Enter edges (u v capacity):")

for i in range(e):
    u, v, c = input(f"Edge {i+1}: ").split()
    graph[u][v] = int(c)

source = input("Enter source vertex: ")
sink = input("Enter sink vertex: ")

max_flow = ford_fulkerson(graph, source, sink)

print("\nMaximum Flow from", source, "to", sink, "=", max_flow)
print("Experiment executed successfully.")
