#q. print odd no:s btwn initial and final, and the numbrs must divsble by 3

initial=int(input("enter the number"))
final=int(input("enter the number"))

# method 1

# i=initial
# while(i<=final):
#     if(i%2!=0 and i%3==0):
#         print(i)
#     i+=1


# method 2

while(initial<=final):
    if(initial%2!=0 and initial%3==0):
        print(initial)
    initial+=1