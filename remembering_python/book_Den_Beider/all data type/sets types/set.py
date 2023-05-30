# create
# {1, 2}, set()

arr = ["Mike", "Tatyana", "Tom", "Mike", "Tom", "Tom", "Tatyana"]
set_arr = set(arr)
print(set_arr)  # {'Mike', 'Tatyana', 'Tom'}
print(len(set_arr))  # 3
print("Tatyana" in set_arr)  # True
if "Tom" in set_arr:
    set_arr.remove("Tom")
print(set_arr)  # {'Mike', 'Tatyana'}
