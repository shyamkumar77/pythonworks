import re

# fullmatch(): returns a Match object if the whole string matches the search pattern of a regular expression

# checking phone number validation
# x='[0-9]{10}' #the rule: digits btwn 0-9 and quantifier {10} means only 10 numbers allowed
# s=input("enter the string to validate")
#
# matcher=re.fullmatch(x,s)
# if matcher is not None: # if matcher not none means the match is there
#     print("valid")
# else:
#     print("invalid")
# print("*"*100)

# indian numbers validation rule

# x='[+][9][1][0-9]{10}'
# s=input("enter the string to validate")
#
# matcher=re.fullmatch(x,s)
# if matcher is not None:
#     print("valid")
# else:
#     print("not valid")
print("## "*100)

# kerala vehicle validation : KL17QC5673

# x='[K][L][0-9]{2}[A-Z]{2}[0-9]{4}'
# s=input("enter the string to validate")
#
# matcher=re.fullmatch(x,s)
# if matcher is not None:
#     print("valid")
# else:
#     print("not valid")
# print("^^ "*100)

# rule: start with a and end with b

# x='^a[\w\W]*b$' # starts with a(^a) and ends with b(b$) in btwn anything (\w\W),  (*) it match count when 0 or whatever it is
# s=input("enter the string to validate")
#
# matcher=re.fullmatch(x,s)
# if matcher is not None:
#     print("valid")
# else:
#     print("not valid")
print("%% "*100)

# rule: numbers or special characters with string count 5
# x='[\d\W]{5}'
# s=input("enter the string to validate")
#
# matcher=re.fullmatch(x,s)
# if matcher is not None:
#     print("valid")
# else:
#     print("not valid")
print("^^ "*100)

# rule: string with uppercase and lowercase
#        minimum count 3  maximum 6

# x='[a-zA-Z]{3,6}'
# s=input("enter the string to validate")
#
# matcher=re.fullmatch(x,s)
# if matcher is not None:
#     print("valid")
# else:
#     print("not valid")
print("&& "*100)

# rule: string starts and ends with 0
#       minimum count 5 and maximum 10

# x='^0[\w\W]{3,8}0$' # starts with 0 and end with 0 inbtwn anything(\w\W) with limit{3,8}
# s=input("enter the string to validate")
#
# matcher=re.fullmatch(x,s)
# if matcher is not None:
#     print("valid")
# else:
#     print("not valid")
print("00 "*100)

# rule: string with special characters
#       last elemnt must a  number or small letter
#       exact count 4

x='\W{3}[a-z\d]'  # here special characters 3 with small letter or digit by default 1
s=input("enter the string to validate")

matcher=re.fullmatch(x,s)
if matcher is not None:
    print("valid")
else:
    print("not valid")


