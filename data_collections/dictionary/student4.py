students=['anu','amal','binoy','ravi']

# from the list make dictnry with names as keys and values as roll numbrs from 1 to 4

# dic={}
#
# roll=1
# for i in students:
#     dic.update({i:roll})
#     roll+=1
#
# print(dic)

# or


student={}  # creating a new dic
roll=1

for i in students:
    student[i]=roll
    roll+=1

print(student)