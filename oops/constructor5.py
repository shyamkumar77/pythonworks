# constructor: used to initialize objects at the time of object creation
# advntage: the portion to call a method is reduced
#
class Person:
    def __init__(self,name,age,place):  # __init__ : the constructor
        self.name=name
        self.age=age
        self.place=place

    def printdata(self):
        print(self.name,self.age,self.place)

pe1=Person("shyam",22,"kochi")  # initializing values during object creation
pe1.printdata()

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


class Employee:
    company="google"
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def printemploy(self):
        print(self.name,self.age,self.place,Employee.company)

emp1=Employee("shyam",23,"ekm")
emp1.printemploy()










