# Author: Jigesh Sheoran
# SAP ID: 590025428
# Experiment: DFS for Shortest Path
# Course: M.Sc. Cyber Security – Semester 1

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


