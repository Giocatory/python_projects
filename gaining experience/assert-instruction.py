try:
    some_numbers = [1, 2, 3, 4, 5, 6, 7]
    assert some_numbers == [1, 2, 3, 4, 5, 6], "number is not equal"
except AssertionError as e:
    print(e)

# number is not equal
