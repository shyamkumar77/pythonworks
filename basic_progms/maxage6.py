#q . print name of person with maximum age

person=[("anu",23),("amal",21),("arun",26),("vineeth",22)]

age=[]

for i in person:
    age.append(i[1])

maxage=max(age)
print(maxage)  # 26

for i in person:
    if i[1]==26:
        print(i[0])










