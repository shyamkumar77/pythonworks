# create object for student.txt file ie, by reading from a file
# refer to student.txt

class Student:
    def __init__(self,name,roll,mark):
        self.name=name
        self.roll=roll
        self.mark=mark

    def printvalues(self):
        print(self.name,self.roll,self.mark)


f = open('student.txt', 'r')

for i in f: #amal,1,878
    data=i.rstrip("\n").split(",") #[amal,1,878]
    #print(data)
    name=data[0] #name=amal
    roll=data[1] #roll=1
    mark=data[2] #mark=878

    s1=Student(name,roll,mark)  # it must be inside the loop
    s1.printvalues()
