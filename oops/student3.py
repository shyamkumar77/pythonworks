# create Student class with name,roll,dept,college
# where college name is same so declare it statically

# two types of variable in oops
# instance variable --> related to methods --> accessed using self
# static variable --> related to class --> accesed using classname

class Student:
    college='Luminar' # declaring statically under class creation, bcoz college is same for all
    def setvalue(self,name,rollnumber,department):
        self.name=name
        self.roll=rollnumber
        self.dept=department

    def printvalue(self):
        print(self.roll,self.name,self.dept,Student.college)  #calling college using class

s1=Student()
s1.setvalue("shyam",110,"science")
s1.printvalue()

s2=Student()
s2.setvalue("amal",111,"commerce")
s2.printvalue()