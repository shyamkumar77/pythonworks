# abstraction: in python is defined as a process of handling complexity
# by hiding unnecessary information from the user

# ABC in abstraction: the module that provides the infrastructure for defining abstract base class
# abc : python has a module called abc, that offers necessary tools for crafting abstract base class

# decorator :  as they allow the extension of an existing function, without any modification to
# the original function  (ie, decorators: used to extend fn without any modification)

# @abstractmethod : A decorator indicating abstract methods.
# pass: it is a keyword which is used as a placeholder for future code

#
# create parent abstract class Car

#abstrcat method ---> mileage   wheels


#child class --> tesla and suzuki

# Abstraction

from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod #decorator: used to make a abstractmethod
    def mileage(self):
        pass
    @abstractmethod
    def wheels(self):
        pass
    @abstractmethod
    def steering(self):
        pass

class Tesla(Car):
    def mileage(self):
        print("tesla has good mileage")

    def wheels(self):
        print("tesla comes with stylish wheels")

    def steering(self):
        print("tesla have smooth steering")

    def design(self):
        print("tesla has nice design")


obj1=Tesla()
obj1.wheels()
obj1.design()
obj1.mileage()

print("*"*100)

class Maruti(Car):
    def mileage(self):
        print("maruti has low mileage")
    def wheels(self):
        print("maruti has average wheels")

    def steering(self):
        print("maruti got average steering")

    def color(self):
        print("maruti comes with variety of colors")

obj2=Maruti()
obj2.mileage()
obj2.wheels()
obj2.color()


