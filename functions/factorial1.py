# factorail of a number using function


#1. without argument

def fact():
    num=int(input("enter the number:"))
    fac=1
    for i in range(1,num+1):
        fac=fac*i
    print(fac)

fact()
fact()

print("*"*100)

# 2. with argument

def fact(num):
    fac=1
    for i in range(1,num+1):
        fac=fac*i
    print(fac)

fact(5)
fact(10)