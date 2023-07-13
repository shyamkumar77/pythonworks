# check given number prime or not


# num = int(input("enter the number:"))
# flag=0
#
# for i in range(2,num):
#     if(num%i==0):
#         flag=1
#         break
#
# if(flag==1):
#     print("not prime")
# else:
#     print("prime")

print("*"*100)

#keynote: for break else concept

''''
for
   break
else

ie, we can use else in for loop, if break works then else dont work. else only works if the break stmnt doesnt work
ie, either break or else will work

'''
# method 2 for prime no:s

num = int(input("enter the number:"))
for i in range(2,num):
    if(num%i==0):
        print('not prime')
        break
else:
    print("prime")