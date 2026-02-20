# Author: Jigesh Sheoran
# Last Modified : 20/02/2026

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping happens, list is already sorted
        if not swapped:
            break
    
    return arr


# user input
n = int(input("Enter number of elements: "))

print("Enter elements:")
arr = list(map(int, input().split()))

sorted_list = bubble_sort(arr)

print("\nSorted List:")
print(sorted_list)

print("\nBubble Sort executed successfully.")
