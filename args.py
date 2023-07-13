# *args:  arguments, if we don't know how many arguments tobe passed use *args

def add(*n):
    return n

print(add(5,6,7)) # *args otpt as tuple

#adding elemnts to tuple
tup=add(5,6,7)

lst=list(tup)
lst.extend([2,3,"shyam","cricket"])
tup=tuple(lst)
print(tup)



