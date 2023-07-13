# tuple()

t=(1,2,3,4) # without bracket same
print(t)
print(type(t))

t1=(5,4,3,2.5,'hai',5,5,5,'hello',True,(1,2,3)) # ordered, duplicate support, heterogeneous, indexing possible, nesting support
print(t1)

print(t1[1:5])  # indexing possible

# t1[0]='hey' # not mutable

for i in t1:
    print(i)