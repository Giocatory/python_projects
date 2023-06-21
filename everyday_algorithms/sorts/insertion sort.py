def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


some_list = [20,23,21,22,18,4,5,22,11,9,1,6,0]
print(insertionSort(some_list))
