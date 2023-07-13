# stack
# last in first out   lifo
# add  push
# remove pop
# display



# size
# 1.push stack is full
# 2. pop stack is empty


stack=[]
size=int(input("enter size of stack:"))
top=0

def push():
    global top
    if(top>=size):
        print('stack is full')
    else:
        e=int(input("enter elemnt to add"))
        stack.append(e)
        top+=1
        print(stack)

def pop():
    global top
    if top==0:
        print('stack is empty')
    else:
        stack.pop()
        top-=1
        print(stack)

while True:
    opt=int(input("select operation\n1. push\n2. pop"))
    if(opt==1):
        push()
    else:
        pop()













