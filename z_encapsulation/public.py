# Encapsulation: wrapping of data and methods within a single unit.

# access modifiers: used to control the visibility of fields, methods in a class

# public access modifier
# protected access modifier (_)
# private access modifier (__)

# public access modifier

class Myclass:
# public data members
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def displayage(self):
        print(self.age)



obj1=Myclass('arun',22)
#accessing public data member
print(obj1.name)

# accessing public member function
obj1.displayage()