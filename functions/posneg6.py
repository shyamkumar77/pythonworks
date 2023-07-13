# check number +ve or -ve using function3


def posneg(n):
    if(n>0):
        return 'positive'
    elif(n==0):
        return 'same'
    else:
        return 'negative'

print(posneg(-1))
print(posneg(0))
a=posneg(5)
print(a)