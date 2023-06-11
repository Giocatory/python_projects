import time
from functools import lru_cache


def fibonacci_one(n):
    if n < 2:
        return n
    return fibonacci_one(n - 1) + fibonacci_one(n - 2)


@lru_cache(maxsize=None)
def fibonacci_two(n):
    if n < 2:
        return n
    return fibonacci_two(n - 1) + fibonacci_two(n - 2)


start_time = time.perf_counter()
print(fibonacci_one(30))
end_time = time.perf_counter()
print(f"Время выполнения без lru: {end_time - start_time}сек")
# 832040
# Время выполнения без lru: 0.08413144099904457сек

start_time = time.perf_counter()
print(fibonacci_two(30))
end_time = time.perf_counter()
print(f"Время выполнения с lru: {end_time - start_time}сек")
# 832040
# Время выполнения с lru: 1.5085999621078372e-05сек
