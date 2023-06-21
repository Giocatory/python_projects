import random


def binarySearch(myList, target):
    first = 0
    last = len(myList) - 1
    found = False
    
    while first <= last and not found:
        mid = (first + last) // 2
        if myList[mid] == target:
            found = True
        elif myList[mid] > target:
            last = mid - 1
        else:
            first = mid + 1
    
    if found:
        return mid
    else:
        return None


myList = [random.randint(-100, 100) for i in range(100000)]
myList.sort()
print(binarySearch(myList, 50))  # 74999
