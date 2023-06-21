def shellSort(arr):
    distance = len(arr) // 2
    while distance > 0:
        for i in range(distance, len(arr)):
            temp = arr[i]
            j = i
            while j >= distance and arr[j - distance] > temp:
                arr[j] = arr[j - distance]
                j -= distance
            arr[j] = temp
        distance = distance // 2
    return arr


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1, 8, 0, 7, 9]
    print(shellSort(arr))
