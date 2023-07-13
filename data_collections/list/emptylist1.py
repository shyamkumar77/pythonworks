# empty list

l=list()
l1=[]

print(type(l))
print(type(l1))

# append(): to add elemnts

l.append(10)
l.append(15)
print(l)

# extend(): to add iterable object

l1=[1,2,3,4]
l1.append([5,6,7])  #in append it takes the whole as a single element
print(l1)

l2=[1,2,3,4]
l2.extend([5,6,7])  # in extend it takes as individual elemnt
print(l2)

