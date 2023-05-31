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