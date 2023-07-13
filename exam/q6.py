# 6.	Create objects of the following file and print the details of student with maximum mark?
# anu,1,bca,200
# rahul,2,bba,177
# vinod,3,bba,187
# ajay,4,bca,198
# maya,5, bba,195       #refer to sample1.txt

class Student:
    def __init__(self,name,roll,course,mark):
        self.name=name
        self.roll=roll
        self.course=course
        self.mark=mark

    def printvalue(self):
        print(self.name,self.roll,self.course,self.mark)


f=open("sample1.txt","r")
for i in f:
    data=i.rstrip("\n").split(',')
    #print(data)
    name=data[0]
    roll=data[1]
    course=data[2]
    mark=data[3]

    obj1=Student(name,roll,course,mark)
    obj1.printvalue()