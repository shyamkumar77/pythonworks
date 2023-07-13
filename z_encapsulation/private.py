# private access modifier: it can only be accessed inside a class

class Myclass:
    def __init__(self,name,roll,branch):
        #privat members
        self.__name=name
        self._roll=roll
        self.__branch=branch

       #private member function
    def __displaydetails(self):
        #accessing private data members
        print(self.__name,self._roll,self.__branch)

     #public member function
    def accessprivatefunctions(self):
        #accessing private member function
        self.__displaydetails()
        #print(self.__branch) #object can accesed only inside class

obj=Myclass("shyam",110,"python")
obj.accessprivatefunctions()
obj.__branch="chemistry" #private variable value not gets changed
obj.accessprivatefunctions()
#print(obj.__branch) not possible



