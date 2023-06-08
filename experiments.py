s = "+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890".split(" ")
s.sort()

s = [[i[0:2], i[2::]] for i in s]
d = {}

for i in s:
    if i[0] not in d:
        d[i[0]] = [i[1]]
    else:
        d[i[0]].append(i[1])

print(*sorted(d.items()),sep="\n")
