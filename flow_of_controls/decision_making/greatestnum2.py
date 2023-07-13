# q. input 2 numbers and print greatest of it

num1 = int(input("enter the number"))
num2=int(input("enter the number"))

if(num1>num2):
    print('num1 is greater',num1)
elif(num2>num1):
    print('num2 is greater',num2)
else:
    print('both are same')