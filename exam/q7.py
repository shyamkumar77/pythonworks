# 7.	Create a valid phone numbers file from the following file?
# +915678905432
# +914567890321
# 765432167
# 123450987765
# +919976532456

import re

rule='[+][9][1] [/d]{10}'

f=open("q7.txt","r")
for i in f:
    data=i.rstrip("\n")
    #print(data)
    matcher=re.fullmatch(rule,data)
    print(matcher)