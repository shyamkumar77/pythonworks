# make all the words in data3.txt to individual elements in a list

f=open('data3.txt', 'r')
lst=[]

for i in f:
    data=i.rstrip("\n").split(" ")
    # print(data)
    lst.extend(data) # if append used it shows as nested list

print(lst)

# getting the word count of elements in the list
count={}
for i in lst:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1

print(count)
