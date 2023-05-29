# Tuple - кортеж, тоже самое, что и список, только нельзя изменить элементы
# методы такие же как и у LIST

# Создаем кортеж
my_tuple = ()
print(my_tuple)  # ()
my_tuple = (1, 2, 3)
print(my_tuple)  # (1, 2, 3)
my_tuple = 1,
print(my_tuple)  # (1,)
my_tuple = tuple("hello")
print(my_tuple)  # ('h', 'e', 'l', 'l', 'o')


# Возврат кортежа из функции
def return_tuple(arr):
    summa: int = 1
    count: int = len(arr)
    for i in arr:
        summa += 1
    return summa, count


my_tuple = return_tuple([1, 2, 3])

# распаковка кортежа
sum_elements, count_elements = my_tuple

print(f"Sum elements: {sum_elements}\nCount elements: {count_elements}")
# Sum elements: 4
# Count elements: 3
