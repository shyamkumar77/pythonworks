# sum of prime numbers in a range

lower=int(input("enter the number:"))
upper=int(input("enter the number:"))

sum=0

# for i in range(lower,upper+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             sum=sum+i
#
#
# print(sum)

print("*"*100)

# sum of non-prime numbers in a range

for i in range(lower,upper+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                sum=sum+i
                break # here j loop gets stopped
        else:
            continue


print(sum)





