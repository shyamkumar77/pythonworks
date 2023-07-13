# fibonacci series: always starts from 0,1

# 0 1 1 2 3 5 8 13 21 34



n1=0
n2=1

for i in range(10): # finding first 10 elemnts
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
