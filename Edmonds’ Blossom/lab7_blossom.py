# Author: Jigesh Sheoran
# Last Modified: 17/02/2026

import networkx as nx

# User Input
G = nx.Graph()

n = int(input("Enter number of vertices: "))
vertices = []

print("Enter vertex names:")
for i in range(n):
    v = input(f"Vertex {i+1}: ").strip()
    vertices.append(v)
    G.add_node(v)

e = int(input("Enter number of edges: "))
print("Enter edges (u v):")

for i in range(e):
    u, v = input(f"Edge {i+1}: ").split()
    G.add_edge(u.strip(), v.strip())

# Blossom Algorithm
matching = nx.algorithms.matching.max_weight_matching(G, maxcardinality=True)

print("\nMaximum Matching:")
for u, v in matching:
    print(f"{u} - {v}")

print("\nSize of Maximum Matching:", len(matching))
print("\nExperiment executed successfully.")
