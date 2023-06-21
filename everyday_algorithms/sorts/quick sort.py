def quickSort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i < pivot]
    greater = [i for i in arr[1:] if i >= pivot]
    return quickSort(less) + [pivot] + quickSort(greater)


arr = [1,5,7,8,9,4,6,8,77,4,55,22,33,42,51,67,81,92,13,10,11]
print(quickSort(arr))
