def true_ip(arr):
    if arr == [0, 0, 0, 0] or arr == [255, 255, 255, 255]:
        return False
    for i in arr:
        if i > 255 or i < 0:
            return False
    return True


def true_mask(arr):
    if any(num < 0 or num > 255 for num in arr):
        print(False)
    else:
        binary_mask = f"{arr[0]:08b}{arr[1]:08b}{arr[2]:08b}{arr[3]:08b}"
        # Check if the subnet mask is valid
        if binary_mask.count('01') == 0:
            return True
        else:
            return False


arr_ip = [int(i) for i in input().split('.')]
arr_mask = [int(i) for i in input().split('.')]
arr_result = []

if true_ip(arr_ip) and true_mask(arr_mask):
    for i in range(len(arr_ip)):
        arr_result.append(arr_ip[i] & arr_mask[i])
else:
    print("Валидация не пройдена")

print(*arr_result, sep='.')
