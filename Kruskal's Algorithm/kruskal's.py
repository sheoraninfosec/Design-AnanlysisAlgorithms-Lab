# Author: Jigesh Sheoran
# Last Modified: 10/02/2026

# disjoint Set 
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])   # path compression
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            if rank[rootX] == rank[rootY]:
                rank[rootX] += 1

# algorithm
def kruskal(vertices, edges):
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}
    mst_cost = 0
    mst_edges = []

    # sort edges by increasing weight
    edges.sort(key=lambda x: x[2])

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_cost += w
            mst_edges.append((u, v, w))

    return mst_cost, mst_edges

# user input
vertices = []
edges = []

n = int(input("Enter number of vertices: "))
print("Enter vertex names:")
for i in range(n):
    vertices.append(input(f"Vertex {i+1}: "))

e = int(input("Enter number of edges: "))
print("Enter edges in format: u v weight")

for i in range(e):
    u, v, w = input(f"Edge {i+1}: ").split()
    edges.append((u, v, int(w)))

mst_cost, mst_edges = kruskal(vertices, edges)

print("\nEdges in Minimum Spanning Tree:")
for u, v, w in mst_edges:
    print(f"{u} - {v} : {w}")

print("\nTotal cost of MST:", mst_cost)
print("Kruskal's Algorithm executed successfully.")
