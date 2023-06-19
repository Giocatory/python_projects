import time
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


start_time = time.perf_counter()
print(fibonacci(30))
end_time = time.perf_counter()
print(f"Время выполнения без lru: {end_time - start_time}сек")
# 832040
# Время выполнения без lru: 2.1371999999075797e-05сек

start_time = time.perf_counter()
print(fibonacci(30))
end_time = time.perf_counter()
print(f"Время выполнения с lru: {end_time - start_time}сек")
# 832040
# Время выполнения с lru: 1.8859999997289378e-06сек
