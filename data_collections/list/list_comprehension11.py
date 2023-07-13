# list comprehension

l=[5,6,7,8,9,10,11]

# square of list
square=[]

for i in l:
   square.append(i**2)

print(square)

# using LC

lst=[2,3,4]
squares=[i**2 for i in l]
print(squares)

# even odd

l1=[2,3,4,5,6,7,8,9,10,11,12,13]
evenlst=[i for i in l1 if(i%2==0)]
oddlst=[i for i in l1 if(i%2!=0)]

print(evenlst)
print(oddlst)

# 1-50elemnts divisble by 10 even no: list

l2=[i for i in range(1,51) if(i%2==0) and (i%5==0)]
print(l2)

