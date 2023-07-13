# error creation: to create error using raise Exception

num1=int(input("enter the number:"))
num2=int(input("enter the number:"))

if num1<num2:
    raise  Exception("negative value error")  # use raise  Exception (stmnt)
else:
    print(num1-num2)