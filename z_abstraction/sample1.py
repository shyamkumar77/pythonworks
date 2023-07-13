# abstraction: in python is defined as a process of handling complexity
# by hiding unnecessary information from the user
# it is one of the core concept of OOP's

# ABC in abstraction: the module that provides the infrastructure for defining abstract base class
# abc : python has a module called abc, that offers necessary tools for crafting abstract base class


# decorator : a decorator can be extremely useful, as they allow the extension of an existing function, without any modification to
# the original function source code (ie, decorators: used to extend fn without any modification)

# @abstractmethod : A decorator indicating abstract methods.
# pass: it is a keyword which is used as a placeholder for future code, it is used when the user doesn't want any code tobe execute

from abc import ABC,abstractmethod

class Parent(ABC): #now it is a abstract class, bcoz it inherits ABC

    @abstractmethod #to make a abstract method
    def a(self):
        pass #main parent class has always no body(pass)
    @abstractmethod
    def b(self):
        pass

class Child1(Parent):
    def a(self):
        print("child 1 A")
    def b(self):
        print("child 1 B")
    def c(self):
        print("child 1 c")

obj=Child1()
obj.a()
obj.b()
obj.c()


#in general, the child class must use the parent abstract class methods(abstract method) and child class can give its
# methods separetely in it


