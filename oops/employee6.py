# create employee class using constructor

class Employee:
    company='Luminar'
    def __init__(self,name,id,desig):
        self.name=name
        self.id=id
        self.desig=desig

    def printemployee(self):
        print(self.id,self.name,self.desig,Employee.company)

emp1=Employee("shyam",1,"developer")
emp1.printemployee()

emp2=Employee("rohit",2,"tester")
emp2.printemployee()