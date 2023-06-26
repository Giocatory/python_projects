def bubbleSort(lst):
    a = lst
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


some_list = [20,23,21,22,18,4,5,22,11,9,1,6,0]
print(bubbleSort(some_list))
