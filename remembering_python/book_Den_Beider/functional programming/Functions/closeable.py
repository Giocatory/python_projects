# Closeable
def outer(a, b, c):
    def inner(x):
        return a*x**2 + b*x + c
    return inner

# 2x^2 + bx + c
evaluate = outer(2, 2, 2)
result = evaluate(3)
print(result)  # 26