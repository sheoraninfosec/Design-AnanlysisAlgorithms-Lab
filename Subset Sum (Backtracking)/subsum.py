# Author: Jigesh Sheoran
# Last Modified : 10 / 03 / 2026
# Experiment: Subset Sum Problem

def subset_sum(arr, target, index, current_subset, results):
    if target == 0:
        results.append(current_subset[:])
        return

    if index >= len(arr) or target < 0:
        return

    # Include current element
    current_subset.append(arr[index])
    subset_sum(arr, target - arr[index], index + 1, current_subset, results)

    # Exclude current element
    current_subset.pop()
    subset_sum(arr, target, index + 1, current_subset, results)


# user input
print("Subset Sum Problem Program")

arr = list(map(int, input("Enter set elements separated by space:\n").split()))
target = int(input("Enter target sum:\n"))

results = []
subset_sum(arr, target, 0, [], results)

if results:
    print("\nSubsets with the given sum:")
    for subset in results:
        print(subset)
else:
    print("\nNo subset found with the given sum.")
