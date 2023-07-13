# functions

# identifier   variables      data
#              function_name


# 1. function with no arguments and no return type

# def add():  # defining function
#     num1=int(input("enter the number: "))
#     num2=int(input("enter the number: "))
#     print("sum: ",num1+num2)
#
# add() # function call
# add()
# add()

############################################################################################

# 2. functions with arguments and no return type
#
# def add(num1,num2):
#     sum=num1+num2
#     print(sum)
#
# #if need to input, gave it outside the function
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
#
# add(a,b) # during fn call pass the variables
# add(5,15)
# add(88,12)

print("*"*100)

###########################################################################################


# 3. function with argument and return type


def add(num1,num2):
    return num1+num2

add(5,6)  # it wont give output, use print()

print(add(5,10))
#or
sum=add(10,25)
print(sum)

#key note:1. code after return statment doesnt work,when return happens the working stops so compiler doesnt consider the next codes
# in function one return statemnt is posiible inside one block, ie, in  if-else block we can give 2 return statmnts
# only single value can be returned using return but num1+num2,num1*num2  is possible

print("*"*100)

def printi(n):
    for i in range(n):
        return i
print(printi(5)) # only 0 prints then stops working bcoz of return statmnts
