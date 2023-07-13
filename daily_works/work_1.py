#Write a python program to return a list,having elements which are product of all the other elements except
# the element in that particular position if the given list
# Ex : i/p   lst=[1,2,3]
# Expecting  o/p  lst=[6,3,2]

lst=[1,2,3,4]
l=[]
total=1
for i in lst:
    total=total*i

for i in lst:
    s=total//i
    l.append(s)
print(l)
