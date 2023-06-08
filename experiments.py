n = [int(i) for i in input().split()]
r = [i for i in range(len(n)) if n.count(n[i]) > 1]
print(*r)
