# Syntax
"""
for variable in sequence:
    instructions

1) variable -> 0,1,2,....,n - variables
2) sequence -> str,list,tuple,set,dict...(all iterables)
"""

# 1
s = "hello"
for i in s:
    print(i, end=" ")
# h e l l o 

# 2
for _ in range(3):
    print(1, end=" ")
# 1 1 1

# 3
d = {1: 0, 2: 1, 3: 2}
for k,v in d.items():
    print(k, v, sep=": ", end="; ")
# 1: 0; 2: 1; 3: 2; 

# 4
print()
n = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j], end="\t")
    print()

# 1	 2	3	
# 4	 5	6	
# 7	 8	9
