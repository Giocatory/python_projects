from abc import ABC, abstractclassmethod


class People(ABC):
    @abstractclassmethod
    def __init__(cls, name, age, gender):
        cls.__name = name
        cls.__age = age
        cls.__gender = gender
    
    # getter
    @property
    def name(self):
        return self.__name
    
    # getter
    @property
    def age(self):
        return self.__age
    
    # getter
    @property
    def gender(self):
        return self.__gender


class Employer(People):
    def __init__(self, name, age, gender, employment="any-key", salary="MROT"):
        super().__init__(name, age, gender)
        self.__employment = employment
        self.__salary = salary
    
    # getter
    @property
    def employment(self) -> str:
        return self.__employment
    
    # setter
    @employment.setter
    def employment(self, emp) -> None:
        self.__employment = emp
    
    # getter
    @property
    def salary(self) -> str:
        return self.__salary
    
    # setter
    @salary.setter
    def salary(self, salary) -> None:
        self.__salary = salary
    
    # dunder str
    def __str__(self) -> str:
        return f"Employ info: \n\t{self.name} is {self.age} ({self.gender})\n\tEmployment: {self.__employment}" \
               f"\n\tSalary: \n\t{self.__salary}\n"


first_worker = Employer("Mikhail", 35, "Male", "System Administrator", "40000")
second_worker = Employer("Alejandro", 30, "Male")
second_worker.salary = 28300.52

print(first_worker)
print(second_worker)

# Employ info: Alejandro is 30 (Male)
# 	Employment: System Administrator
# 	Salary: 3000

# Employ info: Alejandro is 30 (Male)
# 	Employment: any-key
# 	Salary: 28300.52
