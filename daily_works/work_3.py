# Write a python program to print the frequency of each element in a given list
# ex : [1,2,7,7,7,8,2,2,1,1,1]
# o/p : frequencies are
#             '1':4 times
#             '2':3 times
#             '7':3 times
#             '8':1 times

lst=[1,2,7,7,7,8,2,2,1,1,1]
freq={}

for i in lst:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

for key, value in freq.items():
    print(key,":", value,"times")