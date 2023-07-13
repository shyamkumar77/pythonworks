# object oriented programming

# class     :  design/blueprint/structure

# object    :  real-world entity

# reference :  to store object


# example:

class Person:   #class creation
    def read(self):  #method creation,  fn in class is called method.     self an instance keyword used to set instance variable
        print("person is reading")
    def walk(self):
        print("person is walking")

pe1=Person() #object stored to reference(pe1)
pe1.read()
pe1.walk()

pe2=Person() #another object created
pe2.walk()
pe2.read()