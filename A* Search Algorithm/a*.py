# Author: Jigesh Sheoran
# Last Modified : 25 /02 /2026
# Experiment: A* Search Algorithm

import heapq

def a_star(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    parent = {}

    while open_list:
        current_f, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1], g_cost[goal]

        for neighbor, weight in graph[current].items():
            tentative_g = g_cost[current] + weight

            if tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current

    return None, None


# user input
print("A* Search Algorithm Program")

vertices = input("Enter vertices separated by space:\n").split()

graph = {v: {} for v in vertices}

e = int(input("Enter number of edges:\n"))
print("Enter edges in format: u v weight")

for i in range(e):
    u, v, w = input(f"Edge {i+1}: ").split()
    graph[u][v] = int(w)
    graph[v][u] = int(w)   # Assuming undirected graph

heuristic = {}
print("Enter heuristic values for each vertex:")
for v in vertices:
    h = int(input(f"h({v}) = "))
    heuristic[v] = h

start = input("Enter start node:\n")
goal = input("Enter goal node:\n")

path, cost = a_star(graph, heuristic, start, goal)

if path:
    print("\nShortest Path:", " → ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")

print("Program executed successfully.")
