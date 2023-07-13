class Student():
    def __init__(self,name,age,branch):
        self.name=name
        self._age=age
        self.__branch=branch

    def _printbranch(self):
        print(self.__branch)

# obj=Student("rahul",25,"java")
# print(obj.name)
# print(obj._age)
# obj.printbranch()


class Employee(Student):
    def __init__(self,salary,place,name,age,branch,experience):
        super().__init__(name,age,branch)
        self.salary=salary
        self._place=place
        self.__experience=experience

    def printsalary_place(self):
        print(self.salary)
        print(self._place)
        print(self.__experience)

    def printexp(self):
        print(self.__experience)

    def branchprint(self):
        self._printbranch()

#
# obj=Employee(5000,"kochi","shyam",22,"python",7)
#
# print(obj.name)
# print(obj._age)
# obj.printsalary_place()
# obj.printbranch()
# obj.printexp()

class Person(Employee):
    def __init__(self,id,country,mark,salary,place,name,age,branch,experience):
        Employee.__init__(self,salary,place,name,age,branch,experience)
        self.id=id
        self._country=country
        self.__mark=mark

    def printmark(self):
        print(self.__mark)


obj=Person(110,"india",55,75000,"kochi","shyam",22,"python",7)
print(obj._place)


