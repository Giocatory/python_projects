########### Dictionary ###########

# Creating
d1 = dict()  # {}
d2 = {}  # {}
d3 = dict(short='sh', long="lg")  # {'short': 'sh', 'long': 'lg'}
d4 = dict.fromkeys(["a", "b"])  # {'a': None, 'b': None}
d5 = dict.fromkeys(["a", "b"], 100)  # {'a': 100, 'b': 100}
d6 = {a: a**2 for a in range(1,4)}  # {1: 1, 2: 4, 3: 9}
d7 = dict(
    [
        ['one', 1],
        ['two', 3],
        ['three', 3]
    ]
)  # {'one': 1, 'two': 3, 'three': 3}
print(d1,d2,d3,d4,d5,d6,d7,sep="\n")

# обращение по ключу, если ключа нет, то создастся новый
# Но если мы попробуем получить значение с ключом, которого нет в словаре, то Python сгенерирует ошибку KeyError
view_dict: dict = {
    "Father": "Mikhail",
    "Mother": "Tatyana",
    "Children": {
        "first": "",
        "second": ""
    }
}

view_dict["Children"]["first"] = "Margo"
view_dict["Children"]["second"] = "Varvar"
view_dict["Children"]["third"] = "Avro"

print(view_dict["Children"]["third"])  # Avro
# print(view_dict["salary"])  произойдет исключение [KeyError]
if "salary" in view_dict.keys():
    print(view_dict["salary"])
else:
    print("This key not found")  # This key not found

for k, v in view_dict.items():
    print(f"{k}: {v}")
# Father: Mikhail
# Mother: Tatyana
# Children: {'first': 'Margo', 'second': 'Varvar', 'third': 'Avro'}
