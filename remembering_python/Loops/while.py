# Syntax
"""
while condition:
    instruction
"""

n = 10
while n >= 0:
    print(n, end=" ")
    n -= 1
# 10 9 8 7 6 5 4 3 2 1 0 

# May add else block
n = 10
while n >= 0:
    print(n, end=" ")
    n -= 1
else:
    print("\nWhile loop, work end")

# 10 9 8 7 6 5 4 3 2 1 0 10 9 8 7 6 5 4 3 2 1 0 
# While loop, work end