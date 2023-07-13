#q. from a set, get a new set ie, it must be even and divisible by 5

s={2,4,6,8,10,15,20,25,3,80,35,40,4,5,50,55}

s1=set()

for i in s:
    if(i%2==0 and i%5==0):
        s1.add(i)

print(s1)