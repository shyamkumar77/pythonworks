# find correct phnos(10 digits) from phno.txt

f=open('phno.txt','r')

for i in f:
    data=i.rstrip("\n")
    #print(data)

    if len(data)==10:
        print(data)



