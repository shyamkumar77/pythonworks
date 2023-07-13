# 5.	What is method overriding give an example using Books class?


class Bmw:
    def setcar(self,model,color):
        self.model=model
        self.color=color


    def printcar(self):
        print(self.model,self.color)

class Audi(Bmw):
    def setaudi(self,engine,seat):
        self.engine=engine
        self.seat=seat

    def printcar(self):
        print(self.engine,self.seat)

obj1=Audi()

obj1.setaudi("good engine","4 seats")
obj1.setcar(1997,"red")  #last method overirdes the previous one, so this didint print
obj1.printcar()



