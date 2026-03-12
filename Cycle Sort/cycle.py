# Author: Jigesh Sheoran
# Last Modifed : 11 / 03 / 2026
# Experiment: Cycle Sort

def cycle_sort(arr):
    n = len(arr)

    for cycle_start in range(n - 1):
        item = arr[cycle_start]
        pos = cycle_start

        # Find the correct position for the item
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1

        # If item is already in correct position
        if pos == cycle_start:
            continue

        # Skip duplicates
        while item == arr[pos]:
            pos += 1

        # Swap
        arr[pos], item = item, arr[pos]

        # Rotate the rest of the cycle
        while pos != cycle_start:
            pos = cycle_start

            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1

            while item == arr[pos]:
                pos += 1

            arr[pos], item = item, arr[pos]

    return arr

# user input
print("Cycle Sort Program")

arr = list(map(int, input("Enter elements separated by space:\n").split()))

sorted_arr = cycle_sort(arr)

print("\nSorted Array:")
print(sorted_arr)
