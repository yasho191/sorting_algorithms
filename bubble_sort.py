# Bubble Sort
# Time Complexity - O(n^2)
def bubble_sort(arr):
    for j in range(len(arr)):
        for k in range(len(arr)-1-j):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    return arr
    
