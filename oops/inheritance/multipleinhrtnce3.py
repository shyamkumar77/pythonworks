# multiple inheritance
# person    name age place
# child     school phn
# student   roll dept
# final otpt: all combined result


class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Child:
    def setchild(self,school,phn):
        self.school=school
        self.phn=phn

class Student(Person,Child): # Student inherits properties from Person and Child
    def setstudent(self,roll,dept):
        self.roll=roll
        self.dept=dept
    def printstudent(self):
        print(self.roll,self.name,self.age,self.dept,self.phn,self.place,self.school)

s1=Student() # Student objct can call all the methods
s1.setperson("shyam",22,"kochi")
s1.setchild("luminar",9874561233)
s1.setstudent(121,"electrical")
s1.printstudent()

s2=Student()
s2.setperson("rahul",25,"delhi")
s2.setchild("HSS",4562359874)
s2.setstudent(125,"software")
s2.printstudent()