#factorial of a number

num = int(input("enter the number: "))

fac=1
for i in range(1,num+1):
    fac*=i
print(fac)

print("*"*100)

'''
2  6   9 ---> 17
15 11  8  --> 17-2=15   17-6=11   17-9=8

3  1  8 --> 8+1=9   8+3=11  3+1=4
9  11 4


'''