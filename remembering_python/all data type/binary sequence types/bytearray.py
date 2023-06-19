# create
b_one: bytearray = bytearray("taxi", "utf-8")
b_two: bytearray = bytearray("🤦‍♀️👌🤷‍♂️😉😎 emoji", "utf-16", errors="ignore")

print(b_one)  # bytearray(b'taxi')
print(b_two)  # bytearray(b'\xff\xfe>\xd8&\xdd\r @&\x0f\xfe=\xd8L\xdc>\xd87\xdd\r
# B&\x0f\xfe=\xd8\t\xde=\xd8\x0e\xde \x00e\x00m\x00o\x00j\x00i\x00')

print(b_one[2])  # 120
print(str(b_one, "ср866"))  # taxi

###################### Methods ######################

# append(bytes) - добавляет элемент в конец объекта
b_to_app = bytearray('str', 'ascii')
for i in list(bytes("ing", 'ascii')):
    b_to_app.append(i)
print(b_to_app)
