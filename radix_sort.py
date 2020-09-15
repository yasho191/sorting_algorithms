# Radix Sort
# Time complexity = O(d*(n+l))
# d = length of the largest number
# n = length of array
# l = length of containers array


def radix_sort(array):
    # converting integers to string
    array = list(map(str, array))

    # finding out the max length of a number in the arr
    x = [len(i) for i in array]
    max_len = max(x)

    # adding zeros to the numbers to make their length equal to the max_len
    for i in range(len(array)):
        a = array[i]
        array[i] = a.zfill(max_len)

    # print(arr)
    # creating a container for the numbers
    container = [[] for i in range(10)]

    # print(container)
    # segregating numbers based on the units, tens, hundreds .....place
    for j in range(max_len):
        # print(j)
        for k in range(len(array)):
            b = array[k][-(j + 1)]
            container[int(b)].append(array[k])

        # making the array empty to enter the new sequence
        array = []

        # Entering data in the new order in the array
        for l in range(10):
            for m in range(len(container[l])):
                array.append(container[l][m])
        container = [[] for i in range(10)]

    # converting the strings back to integers.
    array = list(map(int, array))
    print(array)
    
    
arr = [100, 300, 700, 900, 1, 30, 50, 70, 1000, 11, 22, 99999, 12345, 6, 7, 33, 4, 0, 8, 0, 14, 67, 2, 3]
radix_sort(arr)
