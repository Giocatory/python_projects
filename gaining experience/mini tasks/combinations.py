# Вы хотите проитерировать по всем возможным комбинациям и
# перестановкам коллекции элементов.
from itertools import permutations

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
