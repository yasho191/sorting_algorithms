def insert_sort(arr):
    for i in range(1, len(arr)):
        j = 0
        while j < i:
            if arr[i] < arr[j]:
                x = arr.pop(i)
                arr.insert(j, x)
            j += 1
    return arr

# Bucket Sort

def bucket_sort(arr):
    # making buckets or partitions for segregating numbers
    buckets = []
    maximum = max(arr)
    inc = int(maximum*0.1)
    for i in range(0, maximum, inc):
        if i == 0:
            a = i
            b = i + inc
        else:
            a = i + 1
            b = i + inc
        buckets.append([a, b])
    # print(buckets)
    # making an 2D empty arr of length equal to length of buckets
    containers = [[] for i in range(len(buckets))]

    # Insert the numbers into right containers
    for i in range(len(arr)):
        for j in range(len(buckets)):
            # print(buckets[j])
            if buckets[j][0] <= arr[i] <= buckets[j][1]:
                containers[j].append(arr[i])
    # print(containers)
    arr = []
    for i in range(len(containers)):
        # Sorting the sub array and then appending it to the main resultant arr.
        containers[i] = insert_sort(containers[i])
        for j in range(len(containers[i])):
            # print(containers[i][j])
            arr.append(containers[i][j])
    # print(arr)
    return arr


arr = [100, 300, 700, 900, 1, 30, 50, 70, 1000, 11, 22, 99999, 12345, 6, 7, 33, 4, 0, 8, 0, 14, 67, 2, 3]
arr1 = bucket_sort(arr)
print(arr1)
