# Author: Jigesh Sheoran
# Last Modified : 13 / 03 / 2026
# Experiment: Kahn's Algorithm (Topological Sort)

from collections import deque

def kahn_topological_sort(graph, vertices):
    indegree = {v: 0 for v in vertices}

    # Calculate in-degrees
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque()

    # Add nodes with in-degree 0
    for v in vertices:
        if indegree[v] == 0:
            queue.append(v)

    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != len(vertices):
        print("Cycle detected in the graph.")
    else:
        print("Topological Order:", topo_order)


# user input
print("Kahn's Algorithm (Topological Sort)")

vertices = input("Enter vertices separated by space:\n").split()
graph = {v: [] for v in vertices}

e = int(input("Enter number of directed edges:\n"))

print("Enter edges in format: u v")

for i in range(e):
    u, v = input(f"Edge {i+1}: ").split()
    graph[u].append(v)

kahn_topological_sort(graph, vertices)
