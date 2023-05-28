# INTEGER
n = 9
f = 3.5
fn = 3.0

# Возвращает двоичное представление целого числа
print(bin(n))  # 0b1001

# Возвращает количество битов, необходимых для представления целого числа в двоичном виде,
# исключая знак и начальные нули
print(n.bit_length())  # 4 (1001)

# Возвращает количество единиц в двоичном представлении абсолютного значения целого числа
print(n.bit_count())  # 2

# Возвращает строку байтов этого числа
print(n.to_bytes(10, byteorder='big'))  # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\t'
print(n.to_bytes(10, byteorder='little'))  # b'\t\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# Возвращает число из строки байтов
print(n.from_bytes(b'\x10\x01\x00\x11', byteorder='big'))  # 268501009

# Преобразование в десятичное число
print(int(f))  # 3
# print(int("12b"))  # ValueError: invalid literal for int() with base 10: '12b'
print(int(True))  # 1

# Преобразование в десятичное число из других систем исчисления
print(int('0b1010', 2))  # 10
print(int('0x1010', 16))  # 4112
print(int('0o1010', 8))  # 520

# Преобразование десятичного числа в другие системы исчисления
print(bin(n))  # 0b1001
print(hex(n))  # 0x3
print(oct(n))  # 0o13

# FLOAT

# Возвращает пару чисел, чьё отношение равно этому числу
print(f.as_integer_ratio())  # (7, 2)

# Является ли значение целым числом
print(f.is_integer())  # False
print(fn.is_integer())  # True

# Перевод из float в шестнадцатеричное число
print(f.hex())  # 0x1.c000000000000p+1

# Перевод из шестнадцатеричного числа в float
print(float.fromhex("0x1.c000000000000p+1"))  # 3.5