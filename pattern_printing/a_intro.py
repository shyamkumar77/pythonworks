
# for understanding the working

for i in range(3):
    for j in range(4):
        if i<2 and j==2:
            break
        else:
            print(i,j)
    else:
        print("out")