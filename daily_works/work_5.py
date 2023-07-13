# Write a program to print the below pattern.
#
# A
# B B
# C C C
# D D D D
# E E E E E

m=65

for i in range(1,6):
    for j in range(i):
        print(chr(m),end=" ")
    m=m+1
    print("")