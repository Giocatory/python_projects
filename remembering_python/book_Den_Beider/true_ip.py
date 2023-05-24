def true_ip(arr):
    if arr == [0, 0, 0, 0] or arr == [255, 255, 255, 255]:
        return False
    for i in arr:
        if i > 255 or i < 0:
            return False
    return True


print(true_ip(input().split(".")))
