def my_range(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


x = []
for i in my_range(1, 15, 2.5):
    x.append(i)


print(x)  # [1, 3.5, 6.0, 8.5, 11.0, 13.5]
