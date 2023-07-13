# 1.	Create a child class Bus that will inherit all of the variables and methods of Vehicle class?

class Vehicle:
    def setvehicle(self,color,mileage,model):
        self.model=model
        self.mileage=mileage
        self.color=color

    def printvehicle(self):
        print(self.model,self.color,self.mileage)

class Bus(Vehicle):
    def setbus(self,tyres,seat):
        self.tyres=tyres
        self.seat=seat

    def printfull(self):
        print(self.model,self.mileage,self.color,self.seat,self.tyres)

b1=Bus()
b1.setvehicle('red',32,1999)
b1.setbus(4,30)
b1.printfull()

