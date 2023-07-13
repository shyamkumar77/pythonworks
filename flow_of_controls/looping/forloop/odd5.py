#q. print odd no:s btwn initial and final, and the numbrs must divsble by 3


initial=int(input("enter the number:"))
final=int(input("enter the number:"))

for i in range(initial,final+1):
    if(i%2!=0 and i%3==0):
        print(i)