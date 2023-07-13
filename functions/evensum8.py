# even numbers sum of user inputting btwn a range

def evensum(low,upp):
    sum=0
    for i in range(low,upp+1):
        if(i%2==0):
            sum=sum+i

    return sum

print(evensum(1,5))
print(evensum(2,10))