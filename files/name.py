# find names that starts with 'a' from name.txt and make into a list

lst=[]

f=open('name.txt','r')
for i in f:
    data=i.rstrip('\n')
    #print(data)
    if data[0]=='a':
        #print(data)
        lst.append(data)


print(lst)





