# Selection Sort
# Time Complexity - O(n^2)
def selection_sort(arr):
    for i in range(len(arr)):
        pointer = arr[i]
        for j in range(i+1, len(arr)):
            if pointer > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
