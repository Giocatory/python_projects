import itertools

# Простая генерация списка

arr = [i for i in range(10)]
print(arr)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr.clear()

# Генерация с условием
arr = [i for i in range(10) if i % 2 == 0]
print(arr)  # [0, 2, 4, 6, 8]
arr.clear()

arr = [i**2 if i % 2 == 0 else i for i in range(10)]
print(arr)  # [0, 1, 4, 3, 16, 5, 36, 7, 64, 9]
arr.clear()

# Генерация с циклом
arr = [i*j for i in range(3) for j in range(3)]
print(arr)  # [0, 0, 0, 0, 1, 2, 0, 2, 4]
arr.clear()

# Генерация вложенных списков
arr = [[i, j] for i in range(3) for j in range(3)]
arr2 = [[i*j for i in range(3)] for j in range(3)]
print(arr)  # [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
print(arr2)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
arr.clear()
arr2.clear()

# Генератор списка с lambda
arr = [(lambda i: i**3)(i) for i in range(10)]
print(arr)  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
arr.clear()

# Генератор списка с itertools
arr = [i for i in itertools.repeat(1, 5)]
print(arr)  # [1, 1, 1, 1, 1]
arr.clear()