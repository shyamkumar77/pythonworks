# swapping prblm

num1 = int(input("enter the num1"))
num2 = int(input("enter the num2"))

print("before swapping",num1)
print("before swapping",num2)

# #method 1
# temp=num1
# num1=num2
# num2=temp

# method 2 : tuple unpacking
# num1,num2=num2,num1

#method 3  #num1=10  num2=20
num1=num1+num2  #10+20=30
num2=num1-num2  #30-20=10
num1=num1-num2  #30-10=20


print("after swapping",num1)
print("after swapping",num2)

