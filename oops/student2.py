# create Student class with name,roll,dept,college

class Student:
    def setvalue(self,name,rollnumber,department,college):
        self.name=name
        self.roll=rollnumber
        self.dept=department
        self.college=college

    def printvalue(self):
        print(self.roll,self.name,self.dept,self.college)

s1=Student()
s1.setvalue("shyam",110,"science","ABC")
s1.printvalue()

s2=Student()
s2.setvalue("amal",111,"commerce","XYZ")
s2.printvalue()

print("*****************************")

class Employee:
    company="Luminartechnolab"
    def setemploy(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def printemploy(self):
        print(self.name,self.age,self.salary,Employee.company)

emp1=Employee()
emp1.setemploy("shyam",23,55000)
emp1.printemploy()

emp2=Employee()
emp2.setemploy("arjun",25,75000)
emp2.printemploy()