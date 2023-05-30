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

#### s.islower()
#### s.isupper()
#### s.isspace()
#### s.istitle()
#### s.upper()
#### s.lower()
#### s.startwith()
#### s.endwith()
#### s.join(список)
#### s.capitalize()
#### s.center(width, [fill])
#### s.ord(символ)
#### s.chr(число)
#### s.count(str, [start], [end])
#### s.expandtabs([tabsize])
#### s.lstirp([chars])
#### s.rstrip([chars])
#### s.strip([chars])
#### s.partition(шаблон)
#### s.swapcase()
#### s.title()
#### s.zfill(width)
#### s.ljust(width, fillchar="")
#### s.rjust(width, fillchar="")