s = "one=1 two=2 three=3".split(" ")

arr = [s[i].split('=') for i in range(len(s))]
d = dict(arr)
for key in d:
    d[key] = int(d[key])
print(*sorted(d.items()))
