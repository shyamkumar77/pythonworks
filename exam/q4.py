# 4.	Create an Animal class using constructor and build a child class  Dog?

class Animal:
    def __init__(self,eyes,legs,skin):
        self.eyes=eyes
        self.legs=legs
        self.skin=skin

class Dog(Animal):
    def __init__(self,speed,sound,eyes,legs,skin):
        super().__init__(eyes,legs,skin)
        self.speed=speed
        self.sound=sound

    def fulldetail(self):
        print(self.sound,self.speed,self.legs,self.skin,self.eyes)

d1=Dog(45,"bark sound",'nice eyes',"soft skin",4)
d1.fulldetail()