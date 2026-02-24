# Author: Jigesh Sheoran
# Last Modified : 24//02/2026

import math

def jump_search(arr, key):
    n = len(arr)
    step = int(math.sqrt(n))   # Optimal jump size
    prev = 0

    # Finding the block where element may be present
    while prev < n and arr[min(step, n) - 1] < key:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search within identified block
    for i in range(prev, min(step, n)):
        if arr[i] == key:
            return i

    return -1


# user input
n = int(input("Enter number of elements (sorted list): "))

print("Enter sorted elements:")
arr = list(map(int, input().split()))

key = int(input("Enter element to search: "))

result = jump_search(arr, key)

if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found.")

print("\nJump Search executed successfully.")
