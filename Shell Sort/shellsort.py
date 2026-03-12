# Author: Jigesh Sheoran
# Last Modified : 12 / 03 / 2026
# Experiment: Shell Sort

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr

# user input
print("Shell Sort Program")

arr = list(map(int, input("Enter elements separated by space:\n").split()))

sorted_arr = shell_sort(arr)

print("\nSorted Array:")
print(sorted_arr)
