#q. input initial and final from user and print no:s divisible by 5

initial=int(input("enter the number"))
final=int(input("enter the number"))

i=initial
while(i<=final):
    if(i%5==0):
        print(i)
    i+=1 #increment shouldbe outside if block, if incremnt is in inside the if block the incremnt hppn only if condtn is true
         #we need to incrmnt even if condtn true or false, so provide in outside if

# other method: not using the initialization variable
print("*"*100)

while(initial<=final):
    if(initial%5==0):
        print(initial)
    initial+=1