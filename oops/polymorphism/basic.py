# # polymorphism
# # many - forms
#
# # methods comes same in a class
# #overloading
# #overriding
#
# # overloading: methods name are same but diff number of arguments
# # exmple:
# class A:
#     def method(self,n):
#         self.n=n
#         print("inside A")
#
# class B(A):
#     def method(self):
#         print("inside B")
#
# objb=B()
# objb.method(15)  # here works method in class A, bcoz one argument present
# objb.method()   # here works method in class B,  bcoz no arguments
# # but recently python does not support method overloading

print("*"*100)

# method overriding: methods names are same and same number of arguments

class Parent:
    def buyphone(self): # 0 arguments
        print("buy nokia")

class Child:
    def buyphone(self): # 0 arguments
        print("buy iphone")
# here 0 arguments with same method name

objc=Child()
objc.buyphone() # here last method always gets executed
# python support method overriding



