# Author: Jigesh Sheoran
# Last Modified: 01/01/2026

from collections import defaultdict, deque

def topological_sort(vertices, edges):
    
    # create adjacency list and indegree dictionary
    graph = defaultdict(list)
    indegree = {v: 0 for v in vertices}

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # insert all vertices with indegree 0 to queue
    queue = deque()
    for v in vertices:
        if indegree[v] == 0:
            queue.append(v)

    topo_order = []

    # process vertices
    while queue:
        node = queue.popleft()
        topo_order.append(node)

        # reduce indegree of adjacent vertices
        for neighbour in graph[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)

    # check for cycle
    if len(topo_order) != len(vertices):
        print("\nGraph contains a cycle. Topological sorting is not possible.")
        return None

    return topo_order


# user input
print("Topological Sorting using Kahn's Algorithm\n")

n = int(input("Enter number of vertices: "))
vertices = []

print("Enter vertex names:")
for i in range(n):
    vertices.append(input(f"Vertex {i+1}: "))

e = int(input("\nEnter number of directed edges: "))
edges = []

print("Enter edges (u v) meaning u → v:")
for i in range(e):
    u, v = input(f"Edge {i+1}: ").split()
    edges.append((u, v))

result = topological_sort(vertices, edges)

if result:
    print("\nTopological Order:")
    print(" → ".join(result))

print("\nExperiment completed successfully.")

