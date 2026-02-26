# Author: Jigesh Sheoran
# Last Modified : 26 / 02 / 2026
# Experiment: Maximum Subarray using Divide & Conquer

def max_crossing_sum(arr, left, mid, right):
    left_sum = float('-inf')
    total = 0

    # Include elements on left of mid
    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)

    right_sum = float('-inf')
    total = 0

    # Include elements on right of mid
    for i in range(mid + 1, right + 1):
        total += arr[i]
        right_sum = max(right_sum, total)

    return left_sum + right_sum


def max_subarray(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    left_max = max_subarray(arr, left, mid)
    right_max = max_subarray(arr, mid + 1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)

    return max(left_max, right_max, cross_max)


# user input
print("Maximum Subarray (Divide & Conquer) Program")

arr = list(map(int, input("Enter array elements separated by space:\n").split()))

result = max_subarray(arr, 0, len(arr) - 1)

print("\nMaximum Subarray Sum:", result)
print("Program executed successfully.")
