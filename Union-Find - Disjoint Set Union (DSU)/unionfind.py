# Author: Jigesh Sheoran
# Last Modified : 20/03/2026
# Experiment: Union-Find / Disjoint Set Union (DSU)

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    # Find with Path Compression
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Union by Rank
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    # Check if two elements are connected
    def connected(self, x, y):
        return self.find(x) == self.find(y)


# user input
n = int(input("Enter number of elements: "))
dsu = DisjointSet(n)

while True:
    print("\n1. Union\n2. Find\n3. Connected\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        x, y = map(int, input("Enter two elements: ").split())
        dsu.union(x, y)
        print("Union performed.")

    elif choice == 2:
        x = int(input("Enter element: "))
        print("Representative:", dsu.find(x))

    elif choice == 3:
        x, y = map(int, input("Enter two elements: ").split())
        if dsu.connected(x, y):
            print("Yes, connected.")
        else:
            print("Not connected.")

    elif choice == 4:
        break

print("\nUnion-Find (DSU) executed successfully.")
