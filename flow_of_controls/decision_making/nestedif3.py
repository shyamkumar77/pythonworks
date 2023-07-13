# nested if : if inside an if

num = 10

if (num > 6):  # 10>6  # if contn wrong, it print its else ie,('not')
    if (num > 9):  # 10>9   #if condtn wrong, it print its else ie,('in else')
        print(num)  # 10
    else:
        print('in else')
else:
    print('not')
print("*"*100)

#using

if num>6 and  num>9:
    print(num)
else:
    print('in else')