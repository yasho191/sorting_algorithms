# Quick Sort
# Time Complexity = O(nlog(n)) worst case = O(n^2)
def quick_sort(arr, left, right):
    if len(arr)==1:
        return arr
    if left < right:
        index = partition(arr, left, right)
        quick_sort(arr, left, index-1)
        quick_sort(arr, index+1, right)


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
    
arr = [100, 300, 700, 900, 1, 30, 50, 70, 1000, 11, 22, 99999, 12345, 6, 7, 33, 4, 0, 8, 0, 14, 67, 2, 3]
print(quick_sort(arr, 0, len(arr)-1))
print(arr)
