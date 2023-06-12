# abs
print(abs(-5))  # 5

# all
print(all([1, 2, 3]))  # True
print(all([1, 2, 3, 0]))  # False
print(all([]))  # True

# any
print(any([1, 2, 3]))  # True
print(any([]))  # False

# ascii
print(ascii('a'))  # 97
print(ascii(object))  # <class 'object'>

# bin
print(bin(10))  # 0b1010

# bool
print(bool(0))  # False
print(bool(1))  # True
print(bool(''))  # False
print(bool(None))  # False

# bytearray
print(bytearray(b'abc'))  # bytearray(b'abc')

# bytes
print(bytes('abc', encoding='utf-8'))  # b'abc'

# callable
print(callable(abs))  # True
print(callable(all))  # True
print(callable(object))  # True
a = 2
print(callable(a))  # False

# dir
print(dir())
# [
#   '__annotations__',
#   '__builtins__',
#   '__cached__',
#   '__doc__',
#   '__file__',
#   '__loader__',
#   '__name__',
#   '__package__',
#   '__spec__',
#   'a'
# ]

# divmod
print(divmod(10, 3))  # (3, 1)
print(divmod(10, 5))  # (2, 0)

# enumerate
for i, v in enumerate('abc'):
    print(f"{i + 1}) {v}")
# 1) a
# 2) b
# 3) c

# eval
print(eval('2*3**2+2*3+2'))  # 26

# exec
exec('print("hello world")')  # hello world

# filter
a = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 6, 67, 8, 9, 8, 7, 65, 4, 3, 2, 34, 5, 67, 8, 765]
a = list(set(filter(lambda x: x % 2 == 0, a)))
print(a)  # [2, 34, 4, 6, 8]

# globals
print(globals())  # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':
# <_frozen_importlib_external.SourceFileLoader object at 0x7fef0c7fd570>, '__spec__': None, '__annotations__': {},
# '__builtins__': <module 'builtins' (built-in)>, '__file__':
# '/media/giocatory/hard_out_disk/python_projects/remembering_python/book_Den_Beider/Functions/some built-in
# features.py', '__cached__': None, 'a': [2, 34, 4, 6, 8], 'i': 2, 'v': 'c'}

# hash
print(hash('abc'))  # 9194773886714491009

# help
help(object)

# id
print(id(object))  # 94488285513728

# isinstance
print(isinstance(1, int))  # True
print(isinstance(1, object))  # True

# iter
a = [1, 2, 3, 4, 5]
for i in iter(a):
    print(i, end=" ")
# 1 2 3 4 5

# locals
print(locals())

# ord
chars = [i for i in range(ord('a'), ord('z') + 1)]
print(*chars)
# 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122

# vars
print(vars())

# zip
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b)))  # [(1, 4), (2, 5), (3, 6)]
print(dict(zip(a, b)))  # {1: 4, 2: 5, 3: 6}
