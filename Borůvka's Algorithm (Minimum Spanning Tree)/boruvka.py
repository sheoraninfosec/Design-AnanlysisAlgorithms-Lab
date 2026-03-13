# Author: Jigesh Sheoran
# Last Modifed : 13 / 03 / 2026
# Experiment: Borůvka's Algorithm

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def boruvka_mst(self):
        parent = []
        rank = []
        cheapest = [-1] * self.V

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        num_trees = self.V
        mst_weight = 0

        while num_trees > 1:

            for i in range(self.V):
                cheapest[i] = -1

            for i, (u, v, w) in enumerate(self.edges):
                set1 = self.find(parent, u)
                set2 = self.find(parent, v)

                if set1 != set2:

                    if cheapest[set1] == -1 or self.edges[cheapest[set1]][2] > w:
                        cheapest[set1] = i

                    if cheapest[set2] == -1 or self.edges[cheapest[set2]][2] > w:
                        cheapest[set2] = i

            for node in range(self.V):
                if cheapest[node] != -1:
                    u, v, w = self.edges[cheapest[node]]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)

                    if set1 != set2:
                        mst_weight += w
                        self.union(parent, rank, set1, set2)
                        num_trees -= 1
                        print(f"Edge {u} - {v} with weight {w} included in MST")

        print("Total MST weight:", mst_weight)


# user input 
print("Borůvka's Algorithm Program")

V = int(input("Enter number of vertices:\n"))
E = int(input("Enter number of edges:\n"))

g = Graph(V)

print("Enter edges in format: u v weight")

for i in range(E):
    u, v, w = map(int, input(f"Edge {i+1}: ").split())
    g.add_edge(u, v, w)

print("\nMinimum Spanning Tree:")
g.boruvka_mst()
