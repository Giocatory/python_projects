n = [i for i in range(int(input()), int(input()) + 1)]
result = [i*(-1) if i % 2 == 0 else i for i in range(len(n))]
print(*result, sep="\n")
