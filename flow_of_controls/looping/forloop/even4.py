#q. print even no:s btwn the limits

initial=int(input("enter the number:"))
final=int(input("enter the number:"))

for i in range(initial,final+1):
    if(i%2==0):
        print(i)


