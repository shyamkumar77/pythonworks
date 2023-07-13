# pair sum, means print the pairs which gave the sum that user provided

sum=int(input("enter the sum:"))

for i in range(6):     #0                  1...................5
    for j in range(6): #0,1,2,3,4 5         0 1 2 3 4 5   #inner loop executes first
        if i+j==sum:
          print(i,j)#(0,1)(0,2) (0,3) (0,4),(0,5)   (1,0) (1,1) (1,2) (1,3) (1,4) (1,5)