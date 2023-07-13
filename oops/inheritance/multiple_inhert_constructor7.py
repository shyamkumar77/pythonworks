# Constructor using in multiple inheritance
# person     name age place
# child       school phno
# student     roll dept


class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Child:
    def __init__(self,school,phn):
        self.school=school
        self.phn=phn

class Student(Person,Child): # Student inherits properties from Person and Child
    def __init__(self,roll,dept,name,age,place,school,phn): #pass variable of both parents
        Person.__init__(self,name,age,place) #if more than one parent we cant use super() so use class name.__init__(self,varblnms)
        Child.__init__(self,school,phn)   # self must be provided inside brakets
        self.roll=roll
        self.dept=dept
    def printstudent(self):
        print(self.roll,self.name,self.age,self.dept,self.phn,self.place,self.school)

s1=Student(12,"engineer","shyam",22,"kochi","luminar",545623558)
s1.printstudent()