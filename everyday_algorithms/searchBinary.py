import random


def searchBinary(myList, item):
    first = 0
    last = len(myList) - 1
    foundFlag = False
    index_result = None
    
    while first <= last and not foundFlag:
        mid = (first + last) // 2
        if myList[mid] == item:
            foundFlag = True
            index_result = mid
        elif myList[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    
    return f"Search result: {foundFlag}\nIndex {item}: {index_result}"


myList = [random.randint(-100, 100) for i in range(100000)]
print(searchBinary(myList, 50))


# Search result: False
# Index 50: None

# Search result: True
# Index 50: 92953