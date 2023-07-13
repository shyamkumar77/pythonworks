# binary search using function

#l=[1,5,2,3,8,9,10]

def binary_search(e,l):
    count=0
    flag=0
    l.sort()
    low=0
    upper=len(l)-1
    while (low<=upper):
        count+=1
        midindex=(low+upper)//2
        if e==l[midindex]:
            flag=1
            break
        elif(e>l[midindex]):
            low=midindex+1
        elif (e<l[midindex]):
            upper=midindex-1

    if flag==1:
        print('present')
    else:
        print('not present')

binary_search(8,[2,3,4,8,9,10])
binary_search(99,[10,2,3,0,40,50])