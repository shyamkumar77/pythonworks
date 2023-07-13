# Multilevel Inheritance

class A:
    def methoda(self):
        print("inside A class")

class B(A):  # B inherits A
    def methodb(self):
        print("inside B class")

class C(B):  # here C inherits B, but it can inherit A also bcoz B inherits A.   therefore A is indirect parent of C
    def methodc(self):
        print("inside C class")

objc=C()  # object of C can access class A,B and C
objc.methoda()
objc.methodb()
objc.methodc()