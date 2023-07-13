# create employee with name,id,designation,companyname(statically)

class Employee:
    company='google'
    #            emp1,shyam,3,developer
    def setvalue(self,name,id,designation):
        self.name=name
        self.id=id
        self.desig=designation

    def printvalue(self):
        print(self.id,self.name,self.desig,Employee.company)

emp1=Employee()
emp1.setvalue("shyam",1,"developer")
emp1.printvalue()

emp2=Employee()
emp2.setvalue(2,"virat","manager")
emp2.printvalue()



