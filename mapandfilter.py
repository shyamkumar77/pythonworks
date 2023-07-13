# map: used to get same number of output corresponding to input
# filter: used to get the necessary output from the input

# syntax: map(function,iterable data)
#         filter(function,iterable data)

#print square of each elemnt
l=[1,2,3,4,5,6]

#creating fn: it must fn with argmnt and return type
def square(n):
    return n**2

new=map(square,l)
print(list(new))  #use list()/set/tuple, other prints location address


#print cube of list

def cube(a):
    return a**3

new2=map(cube,l)
print(list(new2))

print("*"*100)

#print even no:s from list
#filter()

def even(b):
    return  b%2==0

evenlst=filter(even,l)
print(set(evenlst))