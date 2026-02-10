# Author: Jigesh Sheoran
# Last Modified: 10/02/2026
# Assumption: Elements belong to a uniform matroid (any subset is independent)

def greedy_mwis(elements):
    # S1 sort by weight (descending order)
    elements.sort(key=lambda x: x[1], reverse=True)

    independent_set = []
    total_weight = 0

    # S2 greedily select elements
    for elem, weight in elements:
        independent_set.append(elem)
        total_weight += weight

    return independent_set, total_weight

# user input
n = int(input("Enter number of elements: "))
elements = []

print("Enter elements with their weights:")
for i in range(n):
    name, weight = input(f"Element {i+1} (name weight): ").split()
    elements.append((name.strip(), int(weight)))

independent_set, total_weight = greedy_mwis(elements)

print("\nMaximum Weight Maximal Independent Set:")
print(independent_set)
print("Total Weight:", total_weight)
print("\nGreedy algorithm executed successfully.")
