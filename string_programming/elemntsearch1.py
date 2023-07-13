#q. check elemnt present in a string
s='luminar technolab'

a=input("enter the elemnt:")

for i in s:
    if i==a:
        print('present')
        break
else:
    print("not present")


# method 2 : checking element must be single

if a in s:  # in/not in: membership operator
    print("present")
else:
    print('not present')