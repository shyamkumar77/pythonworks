# list[]

l=[23,4,5,6]
print(l)
print(type(l))

l1=[2,3,4.,5,6.,9,'hai',True]
print(l1)

l3=[2,2,2,3,3,3,'hai','hai']
print(l3)

print(l3[0])

for i in l3:
    print(i)

# len()
print(len(l3))


# create a list without duplicate in one line
lst=[1,2,3,4,5,12,3,3,2,1,4,5]

print(list(set(lst)))  # converting to set then to list

