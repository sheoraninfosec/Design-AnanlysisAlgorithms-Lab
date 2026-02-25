# Author: Jigesh Sheoran
# Last Modified : 25/02/2026
# Experiment: Bellman-Ford Algorithm

def bellman_ford(vertices, edges, source):
    # Step 1: Initialize distances
    distance = {v: float('inf') for v in vertices}
    distance[source] = 0

    # Step 2: Relax edges (V-1 times)
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Step 3: Check for negative weight cycle
    for u, v, w in edges:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            print("Graph contains a negative weight cycle.")
            return None

    return distance


# user input 
print("Bellman-Ford Algorithm Program")

vertices = input("Enter vertices separated by space:\n").split()

e = int(input("Enter number of directed edges:\n"))
edges = []

print("Enter edges in format: u v weight")
for i in range(e):
    u, v, w = input(f"Edge {i+1}: ").split()
    edges.append((u, v, int(w)))

source = input("Enter source vertex:\n")

result = bellman_ford(vertices, edges, source)

if result:
    print("\nShortest distances from source:")
    for vertex in result:
        print(f"{source} → {vertex} = {result[vertex]}")

print("Program executed successfully.")
