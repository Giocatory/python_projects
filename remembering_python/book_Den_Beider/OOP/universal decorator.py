def universal_decorator(func):
    def wrapper(*args, **kwargs):
        print("Вызов функции:", func.__name__)
        print("Аргументы:", args)
        print("Ключевые аргументы:", kwargs)
        result = func(*args, **kwargs)
        print("Результат:", result)
        return result

    return wrapper


@universal_decorator
def add_numbers(a, b):
    return a + b


@universal_decorator
def multiply_numbers(a, b):
    return a * b


result1 = add_numbers(2, 3)
# Вызов функции: add_numbers
# Аргументы: (2, 3)
# Ключевые аргументы: {}
# Результат: 5

result2 = multiply_numbers(4, 5)
# Вызов функции: multiply_numbers
# Аргументы: (4, 5)
# Ключевые аргументы: {}
# Результат: 20
