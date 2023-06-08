s = "Петя Варвара Венера Василиса Василий Федор"
r = tuple(filter(lambda x: "ва" in x, s.lower().split(" ")))
print(*r)
