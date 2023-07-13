# palindrome program using function3


def palindrome(s):
    if(s[::-1]==s):
        return 'palindrome'
    else:
        return 'not palindrome'

print(palindrome('shyam'))
print(palindrome('malayalam'))