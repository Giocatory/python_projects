n1, n2, n3, n4 = [int(i) for i in input().split('.')]

# Check if any number is outside the valid range
if any(num < 0 or num > 255 for num in [n1, n2, n3, n4]):
    print(False)
else:
    binary_mask = f"{n1:08b}{n2:08b}{n3:08b}{n4:08b}"

    # Check if the subnet mask is valid
    if binary_mask.count('01') == 0:
        print(True)
    else:
        print(False)