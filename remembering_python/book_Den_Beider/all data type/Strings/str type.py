# Литералы строк
var1: str = " "
var2: str = ' '
var3: str = """ """
var4: str = ''' '''

# Concatenation
var1 = "One"
var2 = "Two"
print(var1 + " " + var2)  # One Two

# Indexing
print(var1[1])  # n

# Slicing
var3 = "Hello user"
print(var3[0:5])  # Hello

# Длинна
var4 = "abcdefghijklmnopqrstuvwxyz"  # 26
print(len(var4))

# f str
print(f"{var1} {var2};\n{var3}")
# One Two;
# Hello user

# Строка байтов
var_bits = b'\xd0\xbf\xd1\x20\xd0\xb8\xd0\xb2'
print(var_bits)  # b'\xd0\xbf\xd1\x20\xd0\xb8\xd0\xb2'
print(int.from_bytes(var_bits, 'big'))  # 15041971219311677618
