# Author: Jigesh Sheoran
# Last Modified : 25/02/2026
# Experiment: Exponential Search

def binary_search(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def exponential_search(arr, key):
    n = len(arr)

    # If element is at first position
    if arr[0] == key:
        return 0

    # Find range for binary search by repeated doubling
    i = 1
    while i < n and arr[i] <= key:
        i = i * 2

    # Perform binary search in found range
    return binary_search(arr, i // 2, min(i, n - 1), key)


# user input 
print("Exponential Search Program")

arr = list(map(int, input("Enter sorted elements separated by space:\n").split()))
key = int(input("Enter element to search:\n"))

result = exponential_search(arr, key)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

print("Program executed successfully.")
