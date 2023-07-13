# regular expression: pattern matching

import re

# finditer: it returns the matches from a string

matcher=re.finditer('ab','aaaaaabbbbbabaaaabbbb')  #re.finditer(pattern,string)
#print(matcher) #it shows location address

count=0
for i in matcher:
    print(i.start()) #start(): it shows in which index the match occured
    print(i.group()) #group(): shows which the pattern is here ab
    count+=1 #each time match occcur, count gets added
print("count:",count)



