# protected access modifier: the protected methods and data members can be accesed by the child class and the class from which it derived
                #          : in multiple_inhrtnce case, the class declared protected can only accesed by its child class
 # there is a concept called protected data member in java and c++, but in python case it doesn't work bcoz it is similar to public
                # ie, it can be called inside and outsude of a class(child), that meams no difference btwn public and protected

class Student:
    def __init__(self,name,roll,branch):
        # protected data member
        self._name=name
        self._roll=roll
        self._branch=branch

    def _displayrollandbranch(self): #protected member fn
        print(self._roll,self._branch)




obj=Student("rahul",123,"java")
# accessing using object within the class
print(obj._name)
# accesing protected member fn
print(obj._displayrollandbranch())

print("*"*100)

#derived class: this class can also access private members of its parent(Student) class
class Myclass(Student):
    #constructor
    def __init__(self,salary,name,roll,branch):
        super().__init__(name,roll,branch)
        self._salary=salary


    def displaydetails(self):
        #accesing protected data member of super/parent class
        print(self._name)
        #accessing protected member fn of parent class
        self._displayrollandbranch()

#accessing from child/derived class
myobj=Myclass(50000,"karthik",110,"python")
myobj.displaydetails()
# accesing protected data member of child class using object of its class
print(myobj._salary)








