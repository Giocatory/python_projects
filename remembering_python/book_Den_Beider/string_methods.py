# length
simple_text = "word"
print(len(simple_text))  # 4

# concatenation
second_text = "Hello "
print(second_text + simple_text)  # Hello word

# indexing
print(simple_text[0])  # w
print(simple_text[-1])  # d

# slicing [start:stop:step]
result = second_text[2] + simple_text[1:]
print(result)  # lord
print(result[-1::-1])  # drol

# replace
print(second_text.replace("Hello", "Hi"))  # Hi word

# split
print(second_text.split(" "))  # ['Hello', 'word']

# upper
print(second_text.upper())  # HELLO WORD

# lower
print(second_text.lower())  # hello word

# capitalize
print(second_text.capitalize())  # Hello word

# title
print(second_text.title())  # Hello word

# count
print(second_text.count("o"))  # 1

# startswith
print(second_text.startswith("Hello"))  # True

# endswith
print(second_text.endswith("word"))  # False

# isalnum
text_number = "123"
print(text_number.isalnum())  # True

# isalpha
print(text_number.isalpha())  # False

# isdigit
print(text_number.isdigit())  # True

