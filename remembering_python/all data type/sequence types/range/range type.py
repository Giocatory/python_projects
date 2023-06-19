# Range - перечисление
# range(start, stop, step)

my_range = range(1, 10, 2)
print(my_range)
print(my_range[3])  # 7
print(list(my_range))

# Применение в цикле
for i in my_range:
    print(i, end=' ')
print()
# 1 3 5 7 9

n = 20
while n not in my_range:
    n -= 1
print(n)  # 9
