from abc import ABC, abstractmethod


class Car(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class ChevroletNiva(Car):
    color = ""

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def drive(self):
        print("Driving")

    def stop(self):
        print("Stopping")


niva_red = ChevroletNiva('niva_r', 'red')
niva_blue = ChevroletNiva('niva_b', 'blue')

niva_blue.color = "white blue"
print(niva_blue.name, niva_blue.color)
print(niva_red.name, niva_red.color)
