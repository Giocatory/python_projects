def linearSearch(array, value):
    index = 0
    found = False
    while index < len(array) and not found:
        if array[index] == value:
            found = True
        else:
            index += 1
    
    return index if found else None


arr = [1, 2, 3, 4, 5, 6, 7]
print(linearSearch(arr, 3))  # 2
print(linearSearch(arr, 8))  # None
