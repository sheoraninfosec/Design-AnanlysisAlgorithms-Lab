# Author: Jigesh Sheoran 
# SAPID: 590025428

def partition(arr, low, high):
    pivot = arr[high]  
    i = low - 1        

    for j in range(low, high):
        if arr[j] <= pivot:   #elements <= pivot go left
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  #swap9

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  #

        quick_sort(arr, low, pi - 1)   
        quick_sort(arr, pi + 1, high)  


#user input
arr = list(map(int, input("Enter numbers separated by space: ").split()))

print("Original Array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)
