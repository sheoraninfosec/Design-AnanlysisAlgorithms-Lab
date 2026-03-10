# Author: Jigesh Sheoran
# Last Modified : 10 / 07 / 2026
# Experiment: Graph Coloring Problem

def is_safe(graph, color, v, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


def solve_graph_coloring(graph, m, color, v):
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(graph, color, v, c):
            color[v] = c

            if solve_graph_coloring(graph, m, color, v + 1):
                return True

            color[v] = 0

    return False


# user input / brain
print("Graph Coloring Problem")

n = int(input("Enter number of vertices:\n"))

print("Enter adjacency matrix:")
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

m = int(input("Enter number of colors:\n"))

color = [0] * n

if solve_graph_coloring(graph, m, color, 0):
    print("\nColor assignment for vertices:")
    for i in range(n):
        print(f"Vertex {i} → Color {color[i]}")
else:
    print("\nNo valid coloring possible with given colors.")
