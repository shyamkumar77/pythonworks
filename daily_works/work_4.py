# Write a python program to print the count of pythagorian triplets from an array of integers.
# Like an array is given it should give (a, b, c) 's count if  a²+b²=c²   if present in the array.

lst=[1,2,3,4,5,6,7,8,9]
count=0

for a in lst:
    for b in lst:
        for c in lst:
            #print(a,b,c)
            if a**2+b**2==c**2:
                count+=1

print("count:",count)

