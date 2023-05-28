from decimal import Decimal

# Integer
first_number = 30
second_number: int = 10

# Float
first_float: float = 10.5
second_float = 2.5

# Complex
first_complex: complex = 10 + 5j
second_complex: complex = 9 - 3j

# Decimal
first_decimal: Decimal = Decimal('0.1')
second_decimal: Decimal = Decimal('0.2')

# Int + Float = Float
print(first_number + first_float)  # 40.5

# int / int = float
# int // int = float
print(first_number / second_number)  # 3.0
print(first_number // second_number)  # 3

# Decimal calc
print(0.1 + 0.2)  # 0.30000000000000004
print(Decimal(0.1) + Decimal(0.2))  # 0.3
