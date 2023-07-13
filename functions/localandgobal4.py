# local and global variable

num=50  #global variable

def printnum():
    num=100  #local variable
    print(num)

printnum()
print(num)

print("*"*100)
#####################################################################################

# to make local variable to global use global keyword
#global: used when the variable is getting incremented/changing inside a function
num=110
def getnum():
    global num,x   # now these are global so it can access inside and outside the function
    num=50
    x=70
    print(num)

getnum()
print(num)
print(x)

print("*"*100)
########################################################################################

a=100

def printn():
    global a
    a=200
    print(a)

printn()
print(a)
a=250
printn()
