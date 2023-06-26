q = lambda l: q( [x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []

lst = [1,5,7,8,9,4,6,8,77,4,55,22,33,42,51,67,81,92,13,10,11]
print(q(lst))