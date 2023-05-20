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
