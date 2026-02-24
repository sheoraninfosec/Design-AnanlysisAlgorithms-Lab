# Author: Jigesh Sheoran
# Last Modified : 24/02/2026

def heapify(arr, n, i):
    largest = i          # Assume current node is largest
    left = 2 * i + 1     # Left child index
    right = 2 * i + 2    # Right child index

    # Check if left child exists and is greater
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Step 1: Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # Move current root to end
        heapify(arr, i, 0)               # Heapify reduced heap

    return arr


# user input
n = int(input("Enter number of elements: "))

print("Enter elements:")
arr = list(map(int, input().split()))

sorted_list = heap_sort(arr)

print("\nSorted List:")
print(sorted_list)

print("\nHeap Sort executed successfully.")
