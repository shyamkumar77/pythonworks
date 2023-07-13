
#sorting in  ascending orderto a list

l=[15,3,7,41,33,69,78,45]
#l.sort()
new=[]

while l:  # this condtn true bcoz elemnts in 'l', if empty 'l' then this condtn false
    min=l[0]     #15
    for i in l:  #15        7      3.................
        if(i<min): #15<15   7<15   3<7...............
            min=i           #7      3...........the 3 is the smallest
    new.append(min) # 3 append to new
    l.remove(min) # then remove 3 from min
print(new)

#in descending order using slicing
print(new[::-1])

