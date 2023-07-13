# recursion : functions that calls itself
#disadvantages: debugging is hard, takes more memory

#syntax:

# def recursion():
#     #body of function
#     recursion()   #calling fn inside a fn
# recursion()




# def printhello():
#     print('hello')
#     printhello()  # calling the function inside itself
#
#
# printhello() # so it works maxm recursion then stops
# instead using the loop the recursion continuously works like loop

#to get recursion limit
# import sys
# print(sys.getrecursionlimit())
#

##############################################################################
#prgm to print:
# print hello 1
# hello 2
# hello 3
#........
#.........
# hello 994


count=1
def printhello():
    global count
    print("hello",count)
    count+=1
    printhello()


printhello()

