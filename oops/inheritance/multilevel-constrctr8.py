# Multilevel Inheritance

# person    name age place
# parent    phn
# employee  id desig company


class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Parent(Person):
    def __init__(self,phn,name,age,place):
        super().__init__(name,age,place)  #here we use super().__init__ bcoz only one parent
        self.phn=phn

class Employee(Parent):
    company="Luminar"
    def __init__(self,id,desig,phn,name,age,place):
        super().__init__(phn,name,age,place) #here also super().__init__ bcoz only one parent and need to pass all variablenames
        self.id=id
        self.desig=desig

    def printemployee(self,):
        print(self.id, self.name, self.age, self.desig, self.phn, self.place, Employee.company)

emp1=Employee(1,"engineer",1456324562,"shyam",22,"kochi")
emp1.printemployee()


