# factorial

def fac(n): #5  5-1=4  4-1=3 3-1=2
    if n<=1:
        return n
    else:
        return n*fac(n-1)  # 5*4=20  20*3=60  60*2=120

print(fac(5))
