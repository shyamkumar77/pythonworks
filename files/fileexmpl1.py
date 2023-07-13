# text file

# operations
# 1. read   r
# 2. write  w
# 3. append a


# read:

f=open('data1.txt', 'r')
for i in f:
    #print(i)
    data=i.rstrip("\n")  # to remove extra line
    print(data)