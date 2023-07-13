# empty set using set()

s=set()

# add(): to add elements to set

s.add(5)
s.add(10)
s.add(True)
print(s)
print(type(s))


#remove(): to remove elemnt from set

s1={2,4,6,8,1,3,5,7}
s1.remove(3)
print(s1)

# clear(): delete all elements in set

s1.clear()
print(s1)

# del setname: to delete the set

del s1
print(s1)  #error, bcoz its deletd
