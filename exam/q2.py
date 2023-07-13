# 2. Create an example for three types of inheritance in one program by using Person as main class?

class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Employee(Person):
    def setemployee(self,salary,experience):
        self.salary=salary
        self.experience=experience

    def printemployee(self):
        print(self.name,self.age,self.place,self.salary,self.experience)

# e1=Employee()
# e1.setperson("shyam",22,"kochi")
# e1.setemployee(75000,7)
# e1.printemployee()
# print("*"*100)

class Child(Employee):
    def setchild(self,college,branch):
        self.college=college
        self.branch=branch

    def child_details(self):
        print(self.name,self.age,self.place,self.salary,self.experience,self.college,self.branch)

c1=Child()
c1.setperson("rahul",25,"delhi")
c1.setemployee(85000,9)
c1.setchild("Luminar","python")
c1.child_details()