import copy

arr: list = [1]

# append - добавить в конец элемент
arr.append(2)
arr.append("number")
print(arr)  # [1, 2, 'number']

# extend - расширить список, добавляя в конец элементы другого списка
some_arr: list = ["strings", "line"]
arr.extend(some_arr)
print(arr)  # [1, 2, 'number', 'strings', 'line']

# insert - добавить элемент по индексу
arr.insert(0, "numbers")
print(arr)  # ['numbers', 1, 2, 'number', 'strings', 'line']

# remove - удаляет первый попавшийся элемент равный аргуменету
for i in ['numbers', 'number', 'strings', 'line']:
    if i in arr:
        arr.remove(i)
print(arr)  # [1, 2]

# pop - удаляет первый элемент
# pop(i) - удаляет элемент по индексу
popped_val = arr.pop()
print(popped_val)  # 2
print(arr)  # [1]

# index - показывает индекс первого совпадния
# index(x, start, stop) - показывает индекс "х" в заданом диапазоне
arr.extend([1, 1, 1, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 9, 9, 9])
print(arr)  # [1, 1, 1, 1, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 9, 9, 9]
print(arr.index(6))  # 11

# count - количество элементов в списке
print(arr.count(1))  # 4
print(arr.count(5))  # 2

# Уберем повторения для чистоты
arr = list(set(arr))

# sort - сортировка
# или sort(key=function)
arr.sort()
print(arr)  # [1, 3, 4, 5, 6, 7, 8, 9]
arr.sort(key=lambda x: x % 2 != 0)  # сначала четные
print(arr)  # [4, 6, 8, 1, 3, 5, 7, 9]
arr.sort(key=lambda x: x % 2 != 0, reverse=True)  # сначала нечетные
print(arr)  # [1, 3, 5, 7, 9, 4, 6, 8]

# reverse - переворачивает список
arr.reverse()
print(arr)  # [8, 6, 4, 9, 7, 5, 3, 1]

# copy - поверхностное копирование
arr_copy = arr.copy()
print(arr_copy)  # [8, 6, 4, 9, 7, 5, 3, 1]

# Для полного копирования
arr_copy = copy.deepcopy(arr)
print(arr_copy)  # [8, 6, 4, 9, 7, 5, 3, 1]

# clear - удаляет все элементы
arr.clear()
arr_copy.clear()
some_arr.clear()

print(arr)  # []
print(arr_copy)  # []
print(some_arr)  # []
