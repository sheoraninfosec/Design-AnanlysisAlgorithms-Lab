# Author: Jigesh Sheoran
# SAP ID: 590025428
# Experiment: Permutations & Combinations Generator
# Course: M.Sc. Cyber Security – Semester 1

def generate_permutations(arr, start):
    if start == len(arr):
        print(arr)
        return

    for i in range(start, len(arr)):
        arr[start], arr[i] = arr[i], arr[start]
        generate_permutations(arr, start + 1)
        arr[start], arr[i] = arr[i], arr[start]  # backtrack


def generate_combinations(arr, index, current):
    if index == len(arr):
        print(current)
        return

    # Include element
    generate_combinations(arr, index + 1, current + [arr[index]])

    # Exclude element
    generate_combinations(arr, index + 1, current)


# -----------------------------
# Main Program
# -----------------------------
print("Permutations & Combinations Generator")

arr = input("Enter elements separated by space:\n").split()

print("\nPermutations:")
generate_permutations(arr, 0)

print("\nCombinations:")
generate_combinations(arr, 0, [])
