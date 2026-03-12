# Author: Jigesh Sheoran
# Last Modifed : 12 / 03 / 2026
# Experiment: Bucket Sort

def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Put elements into buckets
    for num in arr:
        index = int(num * n)
        buckets[index].append(num)

    # Sort individual buckets
    for bucket in buckets:
        bucket.sort()

    # Concatenate buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# user input
print("Bucket Sort Program")

arr = list(map(float, input("Enter decimal numbers between 0 and 1 separated by space:\n").split()))

sorted_arr = bucket_sort(arr)

print("\nSorted Array:")
print(sorted_arr)
