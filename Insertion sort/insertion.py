# Author: Jigesh Sheoran
# Last Modified : 23/02/2026

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# user input
n = int(input("Enter number of elements: "))

print("Enter elements:")
arr = list(map(int, input().split()))

sorted_list = insertion_sort(arr)

print("\nSorted List:")
print(sorted_list)

print("\nInsertion Sort executed successfully.")
