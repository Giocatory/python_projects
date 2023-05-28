values_arr = ["text", 1, 1.5, 1j, object, True, [], {'one': 1}, {1, 2}, None, (), """""", range(10), b"/x10"]

for i in values_arr:
    print(f"{i} is of type {type(i)}")

"""
text is of type <class 'str'>
1 is of type <class 'int'>
1.5 is of type <class 'float'>
1j is of type <class 'complex'>
<class 'object'> is of type <class 'type'>
True is of type <class 'bool'>
[] is of type <class 'list'>
{'one': 1} is of type <class 'dict'>
{1, 2} is of type <class 'set'>
None is of type <class 'NoneType'>
() is of type <class 'tuple'>
 is of type <class 'str'>
range(0, 10) is of type <class 'range'>
b'10' is of type <class 'bytes'>
"""

"""
Числовые типы:
    int - целые числа
    float - дробные числа
    Decimal - десятичные числа, высокой точности
    complex - комплексные числа

Типы последовательности:
    list - список
    tuple - кортеж
    range - последовательность

Типы текстовой последовательности:
    str - строка
    
Двоичные типы последовательностей:
    bytes - байты
    bytearray - байтовая последовательность
    memoryview - память
    
Типы наборов:
    set - множество
    frozenset - неизменяемое множество

Типы сопоставления:
    dict - словарь
    
Типы аннотаций:
    Generic Alias - генерируемый алиас
    Union - объединение

Тип файлов:
    File - файл
    
Догический тип:
    boolean - логический тип
"""