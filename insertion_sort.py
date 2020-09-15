# Insertion Sort
# Time complexity = O(n^2)
def insert_sort(arr):
    for i in range(1, len(arr)):
        j = 0
        while j < i:
            if arr[i] < arr[j]:
                x = arr.pop(i)
                arr.insert(j, x)
            j += 1
    return arr
