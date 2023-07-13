# exception handling: to handle the errors
# try: the code that gets error
# except : give the message in except block, what if error occurs

num1=int(input("enter the number:"))
num2=int(input("enter the number:"))

# try:
#     print(num1/num2)  # divison by zero not possible
# except:
#     print("in except")

#########################################################################################

# calling Exception module: to know what kind of error occured

try:
    print(num1/num2)
except Exception as e:
    print(e)  # error: division by zero occured