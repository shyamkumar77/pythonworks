# dictionary

d={'name':'shyam','age':22,'place':'kochi',1:False}
print(d)
print(type(d))
#
# d1={'name':'shyam','age':22,'place':'kochi','name':'akhil','age1':25} # duplicate keys get updated not support but value support
# print(d1)
#
# #values accesed by key
# print(d1['name'])
# print(d1['age'])
#
# d2={'name':'shyam','age':22,'place':'kochi',1:False,2:{1:5,2:8}} # 2 is total key
# print(d2) # nesting support
#

# looping through key and value
for i in d:
    print(i,d[i])


# to get keys and values using imbuild method --> otpt in list form

print(d.keys())
print(d.values())