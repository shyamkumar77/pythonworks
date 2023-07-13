# copy contents in data3.txt to data4.txt

f=open('data3.txt','r')
f1=open('data4.txt','w')  # if new file name given in write operation, it will create as new file
for i in f:
    f1.write(i)


