# Author: Jigesh Sheoran
# Last Modifed : 12 / 03 / 2026
# Experiment: Radix Sort

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy back
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# user input
print("Radix Sort Program")

arr = list(map(int, input("Enter non-negative integers separated by space:\n").split()))

radix_sort(arr)

print("\nSorted Array:")
print(arr)
