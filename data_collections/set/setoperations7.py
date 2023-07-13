# set operations

a={1,2,3,4,5}
b={3,4,5,6,7}

#1. union: combination of elemnts from boths ets
print(a.union(b))


#2. intersection: set of common elemnst from 2 sets
print(a.intersection(b))


#3. difference:

print(a.difference(b)) # removes b's elemnts from a

print(b.difference(a)) # removes a's elemnts from b