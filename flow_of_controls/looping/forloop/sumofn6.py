#q. sum of n natural numbers

num=int(input("enter the number: "))

sum=0
for i in range(1,num+1):
    sum=sum+i  #sum+=i
print(sum)