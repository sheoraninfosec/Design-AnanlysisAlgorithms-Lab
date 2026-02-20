# Author: Jigesh Sheoran
# Last Modified : 20/02/2026

from collections import defaultdict

def dfs_shortest_path(graph, current, destination, visited, path, shortest):
    
    visited.add(current)
    path.append(current)

    if current == destination:
        if shortest[0] is None or len(path) < len(shortest[0]):
            shortest[0] = list(path)
    else:
        for neighbor in graph[current]:
            if neighbor not in visited:
                dfs_shortest_path(graph, neighbor, destination, visited, path, shortest)

    path.pop()
    visited.remove(current)

# user input 
graph = defaultdict(list)

vertices = input("Enter vertices separated by space: ").split()

e = int(input("Enter number of edges: "))
print("Enter edges (u v):")

for i in range(e):
    u, v = input(f"Edge {i+1}: ").split()
    graph[u].append(v)
    graph[v].append(u)   # Undirected graph

source = input("Enter source vertex: ")
destination = input("Enter destination vertex: ")

shortest = [None]
dfs_shortest_path(graph, source, destination, set(), [], shortest)

if shortest[0]:
    print("\nShortest Path using DFS:")
    print(" -> ".join(shortest[0]))
    print("Path Length:", len(shortest[0]) - 1)
else:
    print("No path exists.")

print("\nDFS Shortest Path executed successfully.")

