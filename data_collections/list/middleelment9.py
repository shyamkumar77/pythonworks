# find  middle_element using functn

def middle_elemnt(l):
    index=len(l)//2
    print(l[index])

middle_elemnt([5,4,8,9,3])



print("*"*100)

# elemnt wise updations

l=[1,2,3,4]

l[0]=100  # [100, 2, 3, 4]
l[:3]=[5,6,7]# [5, 6, 7, 4]
l[:3]=[8,8,8,8] # [8, 8, 8, 8, 4]
l[:3]=[6] # [6, 8, 4]




print(l)