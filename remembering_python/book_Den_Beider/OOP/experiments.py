from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class ChevroletNiva(Car):
    def drive(self):
        print("Driving")

    def stop(self):
        print("Stopping")


niva = ChevroletNiva()
niva.drive()
niva.stop()

# Driving
# Stopping
