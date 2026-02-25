# Author: Jigesh Sheoran
# Last Modified : 25/02/2026
# Experiment: Interpolation Search

def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high and key >= arr[low] and key <= arr[high]:

        # If all elements are same
        if arr[high] == arr[low]:
            if arr[low] == key:
                return low
            else:
                return -1

        # Estimate position using interpolation formula
        pos = low + int(((key - arr[low]) * (high - low)) /
                        (arr[high] - arr[low]))

        if arr[pos] == key:
            return pos

        if arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# user input
print("Interpolation Search Program")

arr = list(map(int, input("Enter sorted elements separated by space: ").split()))
key = int(input("Enter element to search: "))

result = interpolation_search(arr, key)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

print("Program executed successfully.")
