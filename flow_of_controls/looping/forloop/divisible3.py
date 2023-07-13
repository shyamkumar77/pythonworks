#q. input initial and final from user and print no:s divisible by 5

initial=int(input("enter the number:"))
final=int(input("enter the number:"))
for i in range(initial,final+1):
    if(i%5==0):
        print(i)



