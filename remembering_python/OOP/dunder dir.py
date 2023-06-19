class MyClass:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __dir__(self):
        # Возвращаем список пользовательских атрибутов и методов
        return ['name', 'name (setter)', 'name(getter)']


my_object = MyClass("Mike")

# Используем функцию dir() для получения списка атрибутов и методов объекта
print(dir(my_object))  # ['name', 'name (setter)', 'name(getter)']
print(my_object.__dir__())  # ['name', 'name (setter)', 'name(getter)']
