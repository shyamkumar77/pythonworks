# check user entered key present in dic or not

d={1:100,2:200,3:300,4:400,5:500}

key=int(input("enter the key:"))

if key in d:  # or can use .keys() method
    print('present')
else:
    print('not present')


# check user entered value  present in dic or not

value=int(input("enter the value:"))

if value in d.values(): #.values() method
    print('present')
else:
    print('not present')