# 2.	Find out a pair of elements which form a particular value as sum from a given array?
# For eg: arr=[2,3,4,5,6] print elements having sum=9
# o/p :   pairs which give sum=9  is (3,6),(4,5)


lst=[2,3,8,1,5,4,6]


for i in lst:
    for j in lst:
        if i+j==9:
            print(i,j)