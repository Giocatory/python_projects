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

