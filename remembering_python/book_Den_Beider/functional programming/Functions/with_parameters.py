# Параметров у функций может быть сколько угодно
def user(name: str, age: int):
    print(f"Hello {name}", end=". ")
    if age < 18: print("Come later")
    if 18 <= age <= 55: print("Welcome to company")
    else: print("Sorry you are old")

user("Mike", 35)
# Hello Mike. Welcome to company

# Параметр по умолчанию
def user(name: str = "unknown-user", age: int = 0):
    print(f"Hello {name}", end=". ")
    if age == 0: 
        print("You don't enter age!")
        return
    if name == "unknown-user":
        print("Please enter name")
        return
    if age < 18: print("Come later")
    if 18 <= age <= 55: print("Welcome to company")
    else: print("Sorry you are old")

user("Mike", 35)  # Hello Mike. Welcome to company
user("Mike")  # Hello Mike. You don't enter age!
user(age=35)  # Hello unknown-user. Please enter name
user()  # Hello unknown-user. You don't enter age!

# Не определенное количество параметров

# returned tuple
def undef1(*args):
    return args

print(undef1(1,2,3,4,5))  # (1, 2, 3, 4, 5)
print(undef1([1,2]))  # ([1, 2],)

def undef2(*args):
    l = []
    l.extend(args)
    return l

print(undef2(1,2,3,4,5))  # [1, 2, 3, 4, 5]

# returned dict
def undef3(**kwargs):
    return kwargs

print(undef3(small="[14;18)", norm="[18;55)", old="[55;100]"))
# {'small': '[14;18)', 'norm': '[18;55)', 'old': '[55;100]'}