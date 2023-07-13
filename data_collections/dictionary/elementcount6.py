# get elemnts count in dictionary  ie, otpt: {10: 3, 20: 2, 30: 2, 40: 2, 50: 1, 70: 1}

l=[10,20,30,10,10,20,30,40,50,40,70]

dic={}

for i in l:
    if i not in dic:
        dic[i]=1
    else:
        val=dic[i]
        val+=1
        dic[i]=val

print(dic)


# or

# for i in l:
#     if i not in dic:
#         dic.update({i:1})
#     else:
#         val=dic[i]
#         val+=1
#         dic.update({i:val})
#
# print(dic)
#








