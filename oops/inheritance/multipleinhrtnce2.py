# Multiple Inheritance: more thane one parents

class A:
    def methoda(self):
        print("inside A class")

class B:
    def methodb(self):
        print("inside B class")

class C(A,B):  # here C inherits A and B's properties
    def methodc(self):
        print("inside C class")

objc=C()  # so object of C can call the methods of A,B and C
objc.methodc()
objc.methoda()
objc.methodb()