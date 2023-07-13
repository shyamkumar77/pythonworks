# quantifiers

# x='a+'  a including group
# x='a*' count including zero number of a
# x='a?' count a as each including zero no of a
# x='a{2}' 2 no of a position
# x='a{2,3}' minimum 2 a and maximum 3 a
# x='^a'  check starting with a
# x='a$' check ending with a

import re

x='a+' # here matches with group of a (atleast one a should be there)
matcher=re.finditer(x,'aaa aaaaa abcd aa ab')
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print("count:",count)
print("## "*100)

x='[abc]+' # here match any of the characters group either a,b,c or abc
matcher=re.finditer(x,'aaa aaaaa abcd aa ab bc')
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print("count:",count)
print("%% "*100)

x='a*' # here match group even if no a is present in string
matcher=re.finditer(x,'aaa aaaaa abcd aa 555 ab')
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print("count:",count)
print("$$ "*100)

x='a?' # here match takes as individual elemnets not as group
matcher=re.finditer(x,'aaa aaaaa abcd aa ab')
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print("count:",count)
print("^^" *100)

x='a{2}' # here match when exact count of a is 2 in a string like aa aaaa(here two groups)
matcher=re.finditer(x,'aaa aaaaa abcd aa ab')
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print("count:",count)
print("!! "*100)

x='a{2,4}' # here matches when there is minimum two a and maxm of 4 a
matcher=re.finditer(x,'aaa aaaaa abcd 545 aa ab a')
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print("count:",count)
print("++ "*100)

x='^a' # matches when starting of a string is a (only at the starting)
matcher=re.finditer(x,'aaa aaaaa abcd aa ab')
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print("count:",count)
print("() "*100)

x='a$' # matches when starting of a string is a (only at the starting)
matcher=re.finditer(x,'aaa aaaaa abcd aa aba')
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print("count:",count)