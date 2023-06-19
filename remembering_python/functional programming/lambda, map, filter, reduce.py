from functools import reduce

# Пример с filter()

my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)  # [4, 6, 10, 12, 14]

# Пример с map()
current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(map(lambda x: x * 2, current_list))
print(new_list)  # [2, 6, 8, 12, 20, 22, 30, 24, 28]

# Пример с reduce()
current_list = [5, 15, 20, 30, 50, 55, 75, 60, 70]
summa = reduce((lambda x, y: x + y), current_list)
print(summa)  # 380

# Лямбда и множественные операторы
current_list = [[10, 6, 9], [0, 14, 16, 80], [8, 12, 30, 44]]
sorted_list = lambda x: (sorted(i) for i in x)
second_largest = lambda x, func: [y[len(y) - 2] for y in func(x)]
result = second_largest(current_list, sorted_list)
print(result)  # [9, 16, 30]
