#q. find common elemnts from both sets and add to new set

s1={1,2,3,4,5}
s2={3,4,5,6,7}

s3=set()

for i in s1:
    if i in s2:
        s3.add(i)



print(s3)

