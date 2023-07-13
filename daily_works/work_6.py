# Write a program to filter the dictionary ,from a dictionary of people’s heights
# and you wanted to filter out anyone below a certain height.
# Let’s filter out anyone less than 170cm.



dic={"shyam":170,"akhil":165,"arun":180,"arjun":145,"virat":168,"dhoni":175,"raina":134}

result={}

for i in dic:
    if dic[i]<170:
        result.update({i:dic[i]})

print(result)

