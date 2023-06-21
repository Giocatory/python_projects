# Interpolation search
def intPolsearch(arr, target):
    index = 0
    low = 0
    high = len(arr) - 1
    found = False
    
    while low <= high and not found:
        mid = (low + high) // 2
        if arr[mid] == target:
            found = True
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    if found:
        return mid
    else:
        return None


arr = [12,33,11,99,22,55,90,28,25,30,10,88,29]
print(intPolsearch(arr, 90))  # 6
print(intPolsearch(arr, 100))  # None
