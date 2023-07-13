# create Person class with name,age,place

class Person:
    def setvalue(self,name,age,place):
        self.name1=name #making argumnts as self bcoz to use in another method
        self.age=age
        self.place=place

    def printvalue(self):
        print(self.name1)
        print(self.age)
        print(self.place)


pe1=Person()
pe1.setvalue('shyam',22,'kochi')
pe1.printvalue()

pe2=Person()
pe2.setvalue('virat',35,'delhi')
pe2.printvalue()


