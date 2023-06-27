# Вы хотите создать список N максимальных или минимальных элементов коллекции.
import heapq


# 1
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

print(heapq.nlargest(3, nums))  # [42, 37, 23]
print(heapq.nsmallest(3, nums))  # [-4, 1, 2]


# 2
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print(cheap)
# [
    # {'name': 'YHOO', 'shares': 45, 'price': 16.35}, 
    # {'name': 'FB', 'shares': 200, 'price': 21.09}, 
    # {'name': 'HPQ', 'shares': 35, 'price': 31.75}
# ]
print(expensive)
# [
    # {'name': 'AAPL', 'shares': 50, 'price': 543.22}, 
    # {'name': 'ACME', 'shares': 75, 'price': 115.65}, 
    # {'name': 'IBM', 'shares': 100, 'price': 91.1}
# ]


# 3
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print(min_price)  # (10.75, 'FB')
print(max_price)  # (612.78, 'AAPL')
