# Multileel Inheritance

# person    name age place
# parent    phn
# employee  id desig company

class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Parent(Person):  # Parent inherits Person
    def setparent(self,phn):
        self.phn=phn

class Employee(Parent): # Employee inherits Parent, where Parent contains properties of Person
    company='Luminartechnolab'
    def setemployee(self,id,desig):
        self.id=id
        self.desig=desig
    def printemployee(self):
        print(self.id,self.name,self.age,self.desig,self.phn,self.place,Employee.company)

emp1=Employee() # object of employee can access Person,Parent and Employee class
emp1.setperson("shyam",22,"kochi")
emp1.setparent(2564789564)
emp1.setemployee(121,"engineer")
emp1.printemployee()