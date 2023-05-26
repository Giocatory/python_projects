number: int = 0

while True:
    query = input()
    if query == "zero":
        number = 0
    if query == "exit":
        break
    if query == "result":
        print(number)
    if query.split()[0] == "add":
        number += int(query.split()[1])
    if query.split()[0] == "minus":
        number -= int(query.split()[1])
    if query.split()[0] == "mul":
        number *= int(query.split()[1])
    if query.split()[0] == "div":
        number //= int(query.split()[1])
