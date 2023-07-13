'''
1. ask user select operation
   1. add
   2. subract
   3. multi
   4. div
   5. stop

1 for add,  then user input 2 numbers and print the result
llry sub, multi, div, stop it must be continued until user chooses any other option

while True(it works untile the condition gets wrong)
'''

def add(num1,num2):
    print(num1+num2)

def sub(num1,num2):
    print(num1-num2)

def mul(num1,num2):
    print(num1*num2)

def div(num1,num2):
    print(num1/num2)

while True: # means loop forever ie, contioniously loop works until condtn gets falsed
    choice=int(input("enter the choice\n1.add\n2.sub \n3.mul \n4.div \n5.stop\n:::"))
    if choice==5:
        break
    elif choice>1 and choice<=4:
        num1=int(input("enter the number:"))
        num2=int(input("enter the number:"))
        if choice==1:
            add(num1,num2)
        elif choice==2:
            sub(num1,num2)
        elif choice==3:
            mul(num1,num2)
        else:
            div(num1,num2)
    else:
        print('invalid choice')


