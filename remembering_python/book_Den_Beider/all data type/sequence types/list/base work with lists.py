# Длинна списка
my_list = ["a", "b", "c", "d", "e"]
print(len(my_list))  # 5

# Индексация
"""
индексы ->              0  1   2   3   4
Эелементы списка ->     a  b   c   d   e
Индексы <-             -5 -4  -3  -2  -1 
"""
print(my_list[0])  # a
print(my_list[-1])  # e
print(my_list[5-3])  # c

# Срезы - [start: stop: step] - [start;stop)
print(my_list[::])  # ['a', 'b', 'c', 'd', 'e']
print(my_list[::-1])  # ['e', 'd', 'c', 'b', 'a']
print(my_list[2:4:1])  # ['c', 'd']
print(my_list[-1:-4:-1])  # ['e', 'd', 'c']
print(my_list[-1::-2])  # ['e', 'c', 'a']

# Операция in
print("a" in my_list)  # True
print("z" in my_list)  # False
print("z" not in my_list)  # True
