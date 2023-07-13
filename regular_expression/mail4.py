# refer to mail.txt

# q. print original mails from mail.txt  ie, mailid ends with @gmail.com

import re
rule='\w+@gmail.com$'

f=open('mail.txt','r')
for i in f:
    data=(i.rstrip("\n"))
    #print(data)

    matcher=re.fullmatch(rule,data)
    if matcher is not None:
        print(data)

