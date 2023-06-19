# Литералы строк
# var1: str = " "
# var2: str = ' '
# var3: str = """ """
# var4: str = ''' '''

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

# Без экранирования
a = "C:\Windows\System32\notepad\tabnine.exe"
b = r"C:\Windows\System32\notepad\tab-nine.exe"
c = "C:\\Windows\\System32\\notepad\\tab-nine.exe"
print(a)
# C:\Windows\System32
# otepad	ab-nine.exe
print(b)  # C:\Windows\System32\notepad\tab-nine.exe
print(c)  # C:\Windows\System32\notepad\tab-nine.exe

# Цикл
text = "Какой-то текст, не принципиально"
for i in text:
    print(i, end="")
print()
# Какой-то текст, не принципиально

if "текст" in text[8:16]:
    print("Текст есть")  # Текст есть
else:
    print("Текст нет")
