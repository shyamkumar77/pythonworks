
que=[]
size=int(input("enter size of que:"))
top=0

def enque():
    global top
    if(top>=size):
        print('que is full')
    else:
        e=int(input("enter elemnt to add"))
        que.append(e)
        top+=1
        print(que)

def deque():
    global top
    if top==0:
        print('que is empty')
    else:
        que.remove(que[0])
        top-=1
        print(que)

while True:
    opt=int(input("select operation\n1. push\n2. pop"))
    if(opt==1):
        enque()
    else:
        deque()



