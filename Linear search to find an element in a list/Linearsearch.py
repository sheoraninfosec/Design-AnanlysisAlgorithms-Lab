# Author: Jigesh Sheoran
# Last Modifed: 20/02/2026

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# user input 
n = int(input("Enter number of elements in the list: "))

print("Enter elements:")
arr = list(map(int, input().split()))

key = int(input("Enter element to search: "))

result = linear_search(arr, key)

if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found in the list.")

print("\nLinear Search executed successfully.")
