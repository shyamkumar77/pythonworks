# conversion: from one collection to other

s={1,5,6,7,4,68,2}

print(list(s))  # set to list
print(tuple(s)) # set to tuple

l=[1,2,3,4,5,6,6,6,2,3,1,7]
print(set(l)) # list to set
print("*"*100)

# from given tuple give otpt as (1,2,3,4)
t=(1,2,3)

l=list(t) # by convrting tuple to list then back to tuple
l.append(4)

t=tuple(l)
print(t)
print("*"*100)


# find last elemnt from set
s={12,4,52,5,36,9,87}
s=tuple(s)
print(s[-1]) # order getting changed


