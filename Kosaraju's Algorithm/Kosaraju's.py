# Author: Jigesh Sheoran
# Last Modified: 10/02/2026

from collections import defaultdict

def dfs(graph, node, visited, stack=None, component=None):
    visited.add(node)
    if component is not None:
        component.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack, component)

    if stack is not None:
        stack.append(node)

def reverse_graph(graph):
    rev = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            rev[v].append(u)
    return rev


# user input
n = int(input("Enter number of vertices: "))
vertices = [input(f"Vertex {i+1}: ") for i in range(n)]

graph = defaultdict(list)
e = int(input("Enter number of directed edges: "))
print("Enter edges (u v):")
for _ in range(e):
    u, v = input().split()
    graph[u].append(v)

# S1 ; first DFS
visited = set()
stack = []
for v in vertices:
    if v not in visited:
        dfs(graph, v, visited, stack)

# S2 ; reverse graph
rev_graph = reverse_graph(graph)

# S3 ; DFS on reversed graph
visited.clear()
print("\nStrongly Connected Components:")
while stack:
    node = stack.pop()
    if node not in visited:
        component = []
        dfs(rev_graph, node, visited, component=component)
        print(component)
