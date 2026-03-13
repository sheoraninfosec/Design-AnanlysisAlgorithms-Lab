# Author: Jigesh Sheoran
# Last Modified : 13 / 03 / 2026
# Experiment: Johnson's Algorithm

import heapq

def bellman_ford(vertices, edges, source):
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist


def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        for v, w in graph[u]:
            if dist[v] > current_dist + w:
                dist[v] = current_dist + w
                heapq.heappush(pq, (dist[v], v))

    return dist


def johnsons_algorithm(vertices, edges):
    new_vertex = "Q"
    vertices.append(new_vertex)

    new_edges = edges.copy()
    for v in vertices:
        if v != new_vertex:
            new_edges.append((new_vertex, v, 0))

    h = bellman_ford(vertices, new_edges, new_vertex)

    vertices.remove(new_vertex)

    reweighted_edges = []
    graph = {v: [] for v in vertices}

    for u, v, w in edges:
        new_w = w + h[u] - h[v]
        graph[u].append((v, new_w))
        reweighted_edges.append((u, v, new_w))

    all_pairs = {}

    for v in vertices:
        d = dijkstra(graph, v)
        all_pairs[v] = {u: d[u] - h[v] + h[u] for u in d}

    return all_pairs


# user input
print("Johnson's Algorithm Program")

vertices = input("Enter vertices separated by space:\n").split()

e = int(input("Enter number of edges:\n"))

edges = []
print("Enter edges in format: u v weight")
for i in range(e):
    u, v, w = input(f"Edge {i+1}: ").split()
    edges.append((u, v, int(w)))

result = johnsons_algorithm(vertices.copy(), edges)

print("\nAll-Pairs Shortest Paths:")
for src in result:
    print(f"{src}: {result[src]}")
