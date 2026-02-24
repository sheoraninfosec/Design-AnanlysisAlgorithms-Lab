# Author: Jigesh Sheoran
# Last Modified : 24/02/2026

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# user input
n = int(input("Enter number of elements: "))

print("Enter elements:")
arr = list(map(int, input().split()))

sorted_list = selection_sort(arr)

print("\nSorted List:")
print(sorted_list)

print("\nSelection Sort executed successfully.")
