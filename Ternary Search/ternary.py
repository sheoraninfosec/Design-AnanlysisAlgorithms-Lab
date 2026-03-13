# Author: Jigesh Sheoran
# Last Modified : 13 / 03 / 2026
# Experiment: Ternary Search

def ternary_search(arr, left, right, key):
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2

        if key < arr[mid1]:
            right = mid1 - 1
        elif key > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1


# user input
print("Ternary Search Program")

arr = list(map(int, input("Enter sorted elements separated by space:\n").split()))
key = int(input("Enter element to search:\n"))

index = ternary_search(arr, 0, len(arr) - 1, key)

if index != -1:
    print(f"\nElement found at index {index}")
else:
    print("\nElement not found")
