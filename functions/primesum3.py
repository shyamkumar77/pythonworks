# get prime numbers sum from user inputting range using function

def primesum(lower,upper):
    sum=0
    for i in range(lower,upper+1):
        for j in range(2,i):
            if(i%j==0):
                #print('not prime')  #otherwise it gets printed
                break
        else:
            sum=sum+i
    print(sum)

# for user inputting
a=int(input('enter the initial range'))
b=int(input('enter the final range'))

primesum(a,b)
primesum(10,20)



