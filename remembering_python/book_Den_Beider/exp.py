res = []
while True:
    n = int(input())
    if n == -1:
        break
    res.append(n)
res.reverse()
print(res[1:])