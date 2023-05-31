##### set.add(value) - добавление во множество
set_to_add = {"one"}
arr_to_add = ["two", "three", "four", "five"]
for element in arr_to_add:
    set_to_add.add(element)
print(set_to_add)  # {'one', 'three', 'two', 'four', 'five'}

##### set.remove(value) - Удалить значение (ЕСЛИ value НЕТ, ТО БУДЕТ ИСКЛЮЧЕНИЕ!!!)
if "three" in set_to_add:
    set_to_add.remove("three")
print(set_to_add)  # {'five', 'two', 'four', 'one'}

##### set.discard(value) Удалить значение (если value нет, то ничего не произойдет)
set_to_add.discard("three")
print(set_to_add)  # {'one', 'two', 'four', 'five'}

##### set.clear() - Очищение множества
set_to_add.clear()
print(set_to_add)  # set()

##### set.union(set2) - объединяет множества и возвращает одно
set_union_one = {1, 2, 3, 4, 6, 7, 8, 11}  # len = 8
set_union_two = {1, 3, 7, 5, 9, 11, 13}  # len = 7
set_union_result = set_union_one.union(set_union_two)
print(set_union_result)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13}  len = 11

##### set.intersection(set2) - Пересечение множеств. Получить элементы котоые есть в обоих set
# можно еще записывать как: set1 & set2
set_intersection_one = {1, 2, 3, 4, 6, 7, 8, 11}  # len = 8
set_intersection_two = {1, 3, 7, 5, 9, 11, 13}  # len = 7
set_intersection_result = set_intersection_one & set_intersection_two
print(set_intersection_result)  # {11, 1, 3, 7}  len = 4

##### set.difference(set2) - Возвращает те элементы, которые есть в первом, но отсутствуют во втором
# можно еще записывать так: set1 - set2
set_diff_one = {1, 2, 3, 4, 6, 7, 8, 11}  # len = 8
set_diff_two = {1, 3, 7, 5, 9, 11, 13}  # len = 7
set_diff_one_result = set_diff_one - set_diff_two
set_diff_two_result = set_diff_two - set_diff_one
print(set_diff_one_result)  # {8, 2, 4, 6}
print(set_diff_two_result)  # {9, 13, 5}

