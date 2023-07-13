#q. sum of even numbers in a range

lower = int(input("enter the number"))
upper = int(input("enter the number"))

sum=0
for i in range(lower,upper+1):
    if(i%2==0):
        sum+=i
print(sum)