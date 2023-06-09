# 1 Create attr
class Some:
    pass

a = Some()
b = Some()

a.element = 5
b.element = 6

print(a.element)  # 5
print(b.element)  # 6

# 2 Create Attr
class Any:
    a = 55
    b = 66


obj = Any()

print(obj.a)  # 55
print(obj.b)  # 66
print(Any.b)  # 66

# 3 Private Attr
class Priv_attr:
    __a = 1
    __b = 2
    
    def get_a(self):
        return self.__a
        
    def get_b(self):
        return self.__b


priv_obj = Priv_attr()
# На прямую вызывать нельзя
print(priv_obj._Priv_attr__a)  # 1
print(priv_obj.get_a())  # 1
print(priv_obj.get_b())  # 2