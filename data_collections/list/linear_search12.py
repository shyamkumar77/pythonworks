# linear search using function

l=[1,5,23,3,8,9,10]


def linearsearch(e):
    for i in l:
        if i==e:
            print('present')
            break
    else:
        print('not present')

linearsearch(8)
linearsearch(99)