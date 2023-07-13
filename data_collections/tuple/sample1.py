employee=(('anu','dev',50000),('amal','dev',57000),('anil','tester',34000))

# print sal>55000
for i in employee:
    if(i[2]>55000):
        print(i)

# print name, working in dev
for i in employee:
    if(i[1]=='dev'):
        print(i[0])


# print min salary employees name
lst=[]
for i in employee:
    lst.append(i[2]) #salary assigned to lst

print(lst)

min_sal=min(lst)
print(min_sal)

for i in employee:
    if(i[2]==min_sal):
        print(i[0])