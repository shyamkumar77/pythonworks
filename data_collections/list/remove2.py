# removing elemnts from list

l=[1,2,3,4,5]
print(l)

# single elemnt

l.remove(2)
l.remove(5)
print(l)

# total elemnts
l.clear()
print(l)

l1=[2,3,4,5,6,[5,6,4,7,[2,1]]]  #nesting possible
print(l1)

# delete list
#del l
print(l) # list gets deleted

# pop(): to reomove elemnt using index
l2=[5,6,7,8]
l2.pop() # reomoves from end
l2.pop(1)  #6 removed

print(l2)
