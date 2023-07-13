# empty dictionary

d={}
# or d=dict()
print(d)
print(type(d))

# update

# adding elemnts to empty dictionary
# method 1: update

d.update({'name':'shyam','age':22}) # must passed in dictionary
print(d)

# method 2

d['place']='kochi'
d['salary']=50000
print(d)