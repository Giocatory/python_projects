s = "osnovnye--metody-----slovarey"
for i in range(2, 100):
    if '-' * i in s:
        s.replace('-' * i, "-")
print(s)