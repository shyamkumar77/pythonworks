from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def leg(self):
        pass

    @abstractmethod
    def eyes(self):
        pass

class Cat(Animal):
    def leg(self):
        print("cat got  4 small legs")

    def eyes(self):
        print("cat have small 2 eyes")

    def speed(self):
        print("cat is not to speedy")

obj1=Cat()
obj1.leg()
obj1.eyes()
obj1.speed()

print("*"*100)

class Elephant(Animal):
    def leg(self):
        print(" elephant has 4 large legs")

    def eyes(self):
        print("Elephant with 2 big eyes")

    def speed(self):
        print("Elephnt can run on 60km/hr")

    def color(self):
        print("elephants mostly in grey color")

obj2=Elephant()
obj2.color()
obj2.eyes()
obj2.leg()
obj2.speed()
