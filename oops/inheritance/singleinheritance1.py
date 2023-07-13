# Single inheritace

#create person class      name age place
# create student class     roll dept
# final otpt as            roll name age dept place

class Person:

    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Student(Person):
    def setstudent(self,roll,dept):
        self.roll=roll
        self.dept=dept
        print(self.roll,self.name,self.age,self.dept,self.place)

s1=Student()
s1.setperson("shyam",22,"kochi")
s1.setstudent(110,"computerscience")

s2=Student()
s2.setperson("rohith",25,"palakkad")
s2.setstudent(11,"electrical")
