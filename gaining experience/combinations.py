# Вы хотите проитерировать по всем возможным комбинациям и
# перестановкам коллекции элементов.
from itertools import combinations_with_replacement, permutations

items = ['a', 'b', 'c', 'd']

for comb in permutations(items):
    print(comb)

# ('a', 'b', 'c', 'd')
# ('a', 'b', 'd', 'c')
# ('a', 'c', 'b', 'd')
# ('a', 'c', 'd', 'b')
# ('a', 'd', 'b', 'c')
# ('a', 'd', 'c', 'b')
# ('b', 'a', 'c', 'd')
# ('b', 'a', 'd', 'c')
# ('b', 'c', 'a', 'd')
# ('b', 'c', 'd', 'a')
# ('b', 'd', 'a', 'c')
# ('b', 'd', 'c', 'a')
# ('c', 'a', 'b', 'd')
# ('c', 'a', 'd', 'b')
# ('c', 'b', 'a', 'd')
# ('c', 'b', 'd', 'a')
# ('c', 'd', 'a', 'b')
# ('c', 'd', 'b', 'a')
# ('d', 'a', 'b', 'c')
# ('d', 'a', 'c', 'b')
# ('d', 'b', 'a', 'c')
# ('d', 'b', 'c', 'a')
# ('d', 'c', 'a', 'b')
# ('d', 'c', 'b', 'a')

# или с 2 элементами (к примеру)

for comb in permutations(items, 2):
    print(comb)

# ('a', 'b')
# ('a', 'c')
# ('a', 'd')
# ('b', 'a')
# ('b', 'c')
# ('b', 'd')
# ('c', 'a')
# ('c', 'b')
# ('c', 'd')
# ('d', 'a')
# ('d', 'b')
# ('d', 'c')

# или с соединением элемента комбинациями (к примеру)
for comb in combinations_with_replacement(items, 4):
    print(comb)

# ('a', 'a', 'a', 'a')
# ('a', 'a', 'a', 'b')
# ('a', 'a', 'a', 'c')
# ('a', 'a', 'a', 'd')
# ('a', 'a', 'b', 'b')
# ('a', 'a', 'b', 'c')
# ('a', 'a', 'b', 'd')
# ('a', 'a', 'c', 'c')
# ('a', 'a', 'c', 'd')
# ('a', 'a', 'd', 'd')
# ('a', 'b', 'b', 'b')
# ('a', 'b', 'b', 'c')
# ('a', 'b', 'b', 'd')
# ('a', 'b', 'c', 'c')
# ('a', 'b', 'c', 'd')
# ('a', 'b', 'd', 'd')
# ('a', 'c', 'c', 'c')
# ('a', 'c', 'c', 'd')
# ('a', 'c', 'd', 'd')
# ('a', 'd', 'd', 'd')
# ('b', 'b', 'b', 'b')
# ('b', 'b', 'b', 'c')
# ('b', 'b', 'b', 'd')
# ('b', 'b', 'c', 'c')
# ('b', 'b', 'c', 'd')
# ('b', 'b', 'd', 'd')
# ('b', 'c', 'c', 'c')
# ('b', 'c', 'c', 'd')
# ('b', 'c', 'd', 'd')
# ('b', 'd', 'd', 'd')
# ('c', 'c', 'c', 'c')
# ('c', 'c', 'c', 'd')
# ('c', 'c', 'd', 'd')
# ('c', 'd', 'd', 'd')
# ('d', 'd', 'd', 'd')