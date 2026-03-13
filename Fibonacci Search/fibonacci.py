# Author: Jigesh Sheoran
# Last Modified : 13 / 03 / 2026
# Experiment: Fibonacci Search

def fibonacci_search(arr, key):
    n = len(arr)

    # Initialize fibonacci numbers
    fibMMm2 = 0
    fibMMm1 = 1
    fibM = fibMMm2 + fibMMm1

    while fibM < n:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    offset = -1

    while fibM > 1:
        i = min(offset + fibMMm2, n - 1)

        if arr[i] < key:
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i

        elif arr[i] > key:
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1

        else:
            return i

    if fibMMm1 and offset + 1 < n and arr[offset + 1] == key:
        return offset + 1

    return -1


# user input
print("Fibonacci Search Program")

arr = list(map(int, input("Enter sorted elements separated by space:\n").split()))
key = int(input("Enter element to search:\n"))

index = fibonacci_search(arr, key)

if index != -1:
    print(f"\nElement found at index {index}")
else:
    print("\nElement not found")
