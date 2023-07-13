# single inheritance using constructor

#create person class      name age place
# create student class     roll dept
# final otpt as            roll name age dept place

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
        print(self.name,self.age,self.place)

class Student(Person):
    def __init__(self,roll,dept,name,age,place): # need to pass arguments of parent class
        super().__init__(name,age,place) # use super().__init__(then pass variable names of parent class)
        self.roll=roll
        self.dept=dept
    def printstudent(self):
        print(self.roll,self.name,self.age,self.place,self.dept)

s1=Student(1,"engineer","shyam",22,"kochi")
s1.printstudent()
s1.printperson()