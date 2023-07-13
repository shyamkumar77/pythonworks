# inheritance : to use properties of one class into another class, properties means methods and variables

# Single Inheritance: child has only one parent

class A:  # parent class/super/base
    def methoda(self,num):
        self.num=num
        print("inside A class")

class B(A): # child class/sub/derived   here B inherits properties of  A
    def methodb(self):
        print("inside B class",self.num)

objb=B() # so object of B can call both class methods
objb.methoda(5)
objb.methodb()









