# split(): to get into word by word

# get the count of the words from the string in new dictionary
# otpt as: {'hello': 2, 'hai': 1, 'luminar': 1}
s='hello hai hello luminar hai hai hello luminar shyam'

dic={}

# data=s.split(' ')  # split otpt as list
# print(data)
#
# for i in data:
#     print(i) # now in word by word

data=s.split(' ')
print(data)

for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

print(dic)


# or
#
# for i in data:
#     if i not in dic:
#         dic[i]=1
#     else:
#         val=dic[i] # value get storde in val
#         val+=1 # value gets incremented
#         dic[i]=val  # value gets updated
#
# print(dic)