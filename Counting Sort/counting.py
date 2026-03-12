# Author: Jigesh Sheoran
# Last Modified : 12 / 03 / 2026
# Experiment: Counting Sort

def counting_sort(arr):
    max_val = max(arr)

    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    # Count frequency
    for num in arr:
        count[num] += 1

    # Cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output

# user input
print("Counting Sort Program")

arr = list(map(int, input("Enter non-negative integers separated by space:\n").split()))

sorted_arr = counting_sort(arr)

print("\nSorted Array:")
print(sorted_arr)
