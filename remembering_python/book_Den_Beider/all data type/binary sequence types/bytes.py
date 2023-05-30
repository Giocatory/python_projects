# s.encode(кодировка) - создание строки байткода
print( "Byte".encode('utf-16') )  # b'\xff\xfeB\x00y\x00t\x00e\x00'

# s.decode(кодировка) - разкодирование строки байт кода
print( b'\xff\xfeB\x00y\x00t\x00e\x00'.decode('utf-16') )  # Byte

# bytes and array
arr = bytes([10,11,31,22])
print( arr )  # b'\n\x0b\x1f\x16'
print( list(arr) )  # [10, 11, 31, 22]
print( list(b'\xff\xfeB\x00y\x00t\x00e\x00') )  # [255, 254, 66, 0, 121, 0, 116, 0, 101, 0]
