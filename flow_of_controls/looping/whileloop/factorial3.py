# factorial of a number

num=int(input("enter the number"))
fac=1

i=1
while(i<=num):
    fac*=i
    i+=1
print(fac)


# method 2

while(num>=fac):
    num*=fac
    fac+=1
print(fac)
