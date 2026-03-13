# Author: Jigesh Sheoran
# Laat Modified : 13 / 03 / 2026
# Experiment: Tarjan's Algorithm (Strongly Connected Components)

def tarjan_scc(graph):
    index = 0
    stack = []
    on_stack = set()
    ids = {}
    low = {}
    sccs = []

    def dfs(node):
        nonlocal index
        ids[node] = index
        low[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in ids:
                dfs(neighbor)
                low[node] = min(low[node], low[neighbor])
            elif neighbor in on_stack:
                low[node] = min(low[node], ids[neighbor])

        if ids[node] == low[node]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == node:
                    break
            sccs.append(scc)

    for node in graph:
        if node not in ids:
            dfs(node)

    return sccs

# user input
print("Tarjan's Algorithm Program")

vertices = input("Enter vertices separated by space:\n").split()

graph = {v: [] for v in vertices}

e = int(input("Enter number of directed edges:\n"))

print("Enter edges in format: u v")

for i in range(e):
    u, v = input(f"Edge {i+1}: ").split()
    graph[u].append(v)

sccs = tarjan_scc(graph)

print("\nStrongly Connected Components:")
for comp in sccs:
    print(comp)
