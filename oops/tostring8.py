# tostring: it is used to convert a object to a string
# if tostring(__str__) not used, while printing object it shows a location address

class Student:
    def setvalue(self,name,rollnumber,department,college):
        self.name=name
        self.roll=rollnumber
        self.dept=department
        self.college=college

    def printvalue(self):
        print(self.roll,self.name,self.dept,self.college)

    def __str__(self):  #tostring method
        return self.name  #it returns name, only string values support
    #   return str(self.roll)  #if integer values tobe provided use str()


s1=Student()
s1.setvalue("shyam",110,"science","ABC")
s1.printvalue()

s2=Student()
s2.setvalue("amal",111,"commerce","XYZ")
s2.printvalue()

print(s1.dept) #calling values using objects
print(s2.college)

# tostring method: to convrt object to string
print(s1)