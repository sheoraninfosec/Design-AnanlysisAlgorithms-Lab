# Author: Jigesh Sheoran
# Last Modified : 24/02/2026
# Algorithm: Floyd–Warshall Algorithm

def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j])
    return dist


# user Input
n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix (use large number like 999 for infinity):")
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = floyd_warshall(graph)

print("\nAll-Pairs Shortest Path Matrix:")
for row in result:
    print(row)
