from decimal import Decimal
import time

a, b, x = 0.1, 0.2, 0.3
start = time.time()
for _ in range(1_000_000):
    x += x * a - b

float_time = time.time() - start

a, b, x = Decimal("0.1"), Decimal("0.2"), Decimal("0.3")
start = time.time()
for _ in range(1_000_000):
    x += x * a - b

decimal_time = time.time() - start

print(round(decimal_time / float_time, 3))