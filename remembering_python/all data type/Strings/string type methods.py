################ String methods ################

#### template
long_text: str = "Long-form texts longreads, where a large volume is combined with a deep dive into a topic, are becoming increasingly popular in print and online publications, as they allow a publication to stand out from the information noise. The study aims to identify the prevalence of longreads in the Russian media and the content and compositional features of these texts. The study includes a monitoring of the publications in the Russian central media, followed by a content analysis of 10 stories from 10 print and online editions. The conclusion of the study: longreads are present in different types of editions, from daily newspapers to niche news websites. As a rule, they are devoted to the description of a new phenomenon; they are between 2 and 4 thousand words long and are constructed according to the composition scheme of alternating examples and generalizations."

#s.find(str, [start], [end]) - поиск подстроки в строке. Возвращает первое вхождение или -1
find_first_substr: str = long_text.find("print"); print(find_first_substr)  # 128
find_first_substr: str = long_text.find("print", 120, 480); print(find_first_substr)  # 128
find_first_substr: str = long_text.find("divide"); print(find_first_substr)  # -1

#### s.rfind(str, [start], [end]) - поиск подстроки в строке. Возвращает последнее вхождение или -1
find_first_substr: str = long_text.rfind("print"); print(find_first_substr)  # 498

#### s.index(str, [start], [end]) - поиск подстроки в строке. Возвращает номер первого вхождения или вызывает VALUEERROR
#### s.rindex(str, [start], [end]) - поиск подстроки в строке. Возвращает номер последнего вхождения или вызывает VALUEERROR
################ Проверять только с "in" ################
if "тип" in long_text:  # True
    print(long_text.index("type"))
# 569

long_text_sub_str: str = long_text[0:61]  # Long-form texts longreads, where a large volume is combined
#### s.replace(шаблон, замена, [maxcount]) - замена шаблона на замену. Maxcount - количество замен (по умолчанию всё)
replacing_str: str = long_text_sub_str.replace("e", "#").replace("a", "#").replace("o", "#")
print(long_text_sub_str)  # Long-form texts longreads, where a large volume is combined
print(replacing_str)  # L#ng-f#rm t#xts l#ngr##ds, wh#r# # l#rg# v#lum# is c#mbin#d

#### s.split(символ или без него) - разбиение строки по разделителю в массив
arr_splitting: list = long_text_sub_str.replace(",", "").split(" ")
print(arr_splitting)  # ['Long-form', 'texts', 'longreads', 'where', 'a', 'large', 'volume', 'is', 'combined', 'w']

#### s.isdigit() - состоит ли строка из цифр
#### s.isalpha() - состоит ли строка из букв
#### s.isalnum() - состоит ли строка из цифр или букв
some_text_words: str = "abcdefg"
some_text_nums: str = "12345"
some_text_words_nums: str = "12ab3ce"

print(some_text_words.isalpha())  # True
print(some_text_nums.isdigit())  # True
print(some_text_words_nums.isalnum())  # True
print(some_text_words.isalnum())  # True
print(some_text_nums.isalnum())  # True

#### s.islower() - состоит ли строка из символов нижнего регистра
#### s.isupper() - состоит ли строка из символов верхнего регистра
lower_str: str = 'abc def'
upper_str: str = 'ABC DEF'
print(lower_str.islower())  # True
print(lower_str.isupper())  # False
print(upper_str.isupper())  # True

#### s.isspace() - состоит ли строка из неотображаемых символов (\t,\n,\r,\f,\v,[space])
print(lower_str.isspace())  # False
print("\n".isspace())  # True

#### s.istitle() - начинаются ли слова в строке с заглавной буквы
not_title_str: str = "aS wf"
title_str: str = "Sa Wf"
print(not_title_str.istitle())  # False
print(title_str.istitle())  # True

#### s.upper() - преобразование символов строки в верхний регистр
print("lower case".upper())  # LOWER CASE

#### s.lower() - преобразование символов строки в нижний регистр
print("UPPER CASE".lower())  # upper case

str_to_how: str = "some text with show, how start and end"
#### s.startwith(str) - начинается ли строка с шаблона str
#### s.endwith(str) - заканчивается ли строка с шаблоном str
print(str_to_how.startswith("some"))  # True
print(str_to_how.endswith("end"))  # True

#### s.join(коллекция) - сборка строки из коллекции с разделителем s
arr_for_joined: list = ["Hello", "user", "nice day"]
tuple_for_joined: tuple = ("Hello", "user", "nice day")
print("->".join(arr_for_joined))  # Hello->user->nice day
print("->".join(tuple_for_joined))  # Hello->user->nice day

str_to_show_change_case: str = "some text with show, how go changed"
#### s.capitalize() - переводит первый символ в верхний регистр, а остальные в нижний
print(str_to_show_change_case.capitalize())  # Some text with show, how go changed

#### s.center(width, [fill]) - возвращает отцентрированную строку по краям которой стоят символы fill (по умолчанию пробел)
str_len: int = len(str_to_show_change_case)
print( str_to_show_change_case.center(str_len * 2, "*") )
# *****************some text with show, how go changed******************

#### s.ord(символ) - перевод символа в его код ASCII
print( ord("A") )  # 65

#### s.chr(число) - код ASCII переводит в символ
print( chr(65 + 1) )  # B

#### s.count(str, [start], [end]) - возвращает количество вхождений str в строке. Можно в диапазоне
str_for_show_count: str = "возвращает количество вхождений str в строке. Можно в диапазоне"
print( str_for_show_count.count("о") )  # 8
print( str_for_show_count.count("о", 11, 21) )  # 2 => "количество"

#### s.expandtabs([tabsize]) - возвращает копию строки, в которой все символы табуляции заменяются одним или несколькоми пробелами. Если tabsize не указан, то 1 таб = 8 пробелов
str_with_tabs: str = "I\tam\tuser"
str_without_tabs: str = str_with_tabs.expandtabs(1)
print( str_with_tabs )  # I	am	user
print( str_without_tabs )  # I am user

str_with_spaces: str = "!               text                   !"
#### s.lstirp([chars]) - удаляет пробельные символы в начале строки
print( str_with_spaces.lstrip("!").lstrip() )  # text                   !

#### s.rstrip([chars]) - удаляет пробельные символы в конце строки
print( str_with_spaces.rstrip("!").rstrip() )  # !               text

#### s.strip([chars]) - удаляет пробельные символы в начале и конце
print( str_with_spaces.strip("!").strip() )  # text

#### s.partition(шаблон) - Возвращает кортеж, содержащий часть перед первым шаблоном, сам шаблон и часть после шаблона.
str_for_partitions: str = "Returns a tuple containing the part before the first pattern, the pattern itself, and the part after the pattern"
print( str_for_partitions.partition("the pattern itself") )
# ('Returns a tuple containing the part before the first pattern, ', 'the pattern itself', ', and the part after the pattern')
#### Если шаблон не найден, то вернет текст и две пустые строки
str_for_partition_lose: str = "Returns a tuple containing the part before the first pattern"
print( str_for_partition_lose.partition("the pattern itself") )
#('Returns a tuple containing the part before the first pattern', '', '')

#### s.swapcase() - переводит символы строки в противоположный регистр
str_for_swap: str = "FirSt wOrD"
print( str_for_swap.swapcase() )  # fIRsT WoRd

#### s.title() - переводит первую букву каждого слова в верхний регистр, остальные в нижний
str_convert_to_title: str = "the pattern itself, and the part after the pattern"
print( str_convert_to_title.title() )  # The Pattern Itself, And The Part After The Pattern

str_to_fill_and_just: str = "welcome"
#### s.zfill(width) - делает строку длинной не менее width, по необходимости заполняя первые символы нулями
print( str_to_fill_and_just.zfill(21) )  # 00000000000000welcome
#### s.ljust(width, fillchar="") - делает строку не менее width, по необходимости заполняя последние символы, символом fillchar
print( str_to_fill_and_just.ljust(21, "*") )  # welcome**************
#### s.rjust(width, fillchar="") - делает строку не менее width, по необходимости заполняя первые символы, символом fillchar
print( str_to_fill_and_just.rjust(21, "*") )  # **************welcome
