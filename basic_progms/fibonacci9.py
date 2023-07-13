# fibonacci series upto user providing limit

terms=int(input("enter the number:"))

n1=0
n2=1

for i in range(terms):
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3