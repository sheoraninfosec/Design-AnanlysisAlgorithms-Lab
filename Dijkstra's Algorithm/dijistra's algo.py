# Author: Jigesh Sheoran
# SAP ID: 590025428 

import heapq  

def dijkstra(graph, start):
    # all other distance is infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0              # Distance to itself = 0

    algo = [(0, start)]  

    while algo:
        current_distance, current_node = heapq.heappop(algo)

        # skip if shorter path is already found
        if current_distance > distances[current_node]:
            continue
        
        # explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # if found a shorter path, update 
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(algo, (distance, neighbor))
    
    return distances

graph = {
    'A': {'B': 3, 'C': 6},
    'B': {'A': 3, 'C': 2, 'D': 1},
    'C': {'A': 6, 'B': 2, 'D': 4, 'E': 2},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 5},
    'E': {'C': 2, 'D': 3, 'F': 1},
    'F': {'D': 5, 'E': 1}
}


start_node = input("Enter starting node (A-F): ").upper()

if start_node not in graph:
    print("Invalid node!")
else:
    shortest_paths = dijkstra(graph, start_node)
    print(f"\nShortest distances from {start_node}:")
    for node, dist in shortest_paths.items():
        print(f"{start_node} → {node} = {dist}")
