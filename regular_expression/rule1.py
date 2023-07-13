# Rules:

# x='[abc]' either a b or c
# x='[^abc]' except abc
# x='[a-z]' a to z
# x='[A-Z]' A to Z
# x='[a-zA-Z]' both lower and upper case are checked
# x='[0-9]' check digits
# x='[^a-zA-Z0-9]' special symbols
# x='\s' check space
# x='\d' check the digits
# x='\D' except digits
# x='\w' all words and digits except special characters
# x='\W' for special characters

import  re

x='[abc]'
matcher=re.finditer(x,'abc 123@ABC')  #finditer(pattern,string)
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start()) #start(): it shows in which index the match occured
    print(i.group()) #group(): shows which the pattern
    count+=1 #each time match occcur, count gets added
print("count:",count)
print("*"*100)

x='[^abc]' # except abc
matcher=re.finditer(x,'abc 123@ABC')
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print("count:",count)
print("** "*100)

x='[^a-zA-Z0-9]' # only matches the special characters
matcher=re.finditer(x,'ab#c% 123@ABC!')
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print("count:",count)
print("#"*100)

x='[\s]' # only matches the space
matcher=re.finditer(x,'ab#c% 123 @ABC!')
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print("count:",count)
print("## "*100)

x='[\d]' # only matches the digits
matcher=re.finditer(x,'ab#c% 123@ABC!')
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print("count:",count)
print("$"*100)

x='[\w]' # except the special characters
matcher=re.finditer(x,'ab#c% 123@ABC!')
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print("count:",count)
print("% "*100)

x='[\W]' # only matches the special characters
matcher=re.finditer(x,'ab#c% 123@ABC!')
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print("count:",count)


