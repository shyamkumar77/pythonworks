# refer to phn.txt

#q. from phn.txt take valid phone numbers and write to newfile

import re

rule='[+][9][1][0-9]{10}'



f=open('phn.txt','r')
f1=open("validphn.txt", 'w')

for i in f:
    phn=i.rstrip("\n")
    #print(phn)
    matcher=re.fullmatch(rule,phn)
    if matcher is not None:
        f1.write(i) # instead of i if 'phn' uses it only takes last number

