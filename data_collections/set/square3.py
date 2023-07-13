# froma a given set, get the square of it to new set

s={1,2,3,4,5,6,7}
square=set()

for i in s:
    square.add(i**2)

print(square)

s1={2,4,6,8,1,3,5,7,{2,4,5}}  #nesting not possible
print(s1)