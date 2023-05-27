stack = []
while True:
    s = input().split()
    match s[0]:
        case "close":
            break
        case "add":
            stack.append(s[1])
        case "pop":
            print(stack.pop())
        case "head":
            print(stack[-1])