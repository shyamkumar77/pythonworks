#q. given a fixed amount, ask user to inpt withdrw amount and print balance
fixed_amount=100000

withdraw=int(input("enter the amount to withdraw"))
balance=fixed_amount-withdraw
print("balance is",balance)
print("*"*100)

# using if else

if(withdraw>fixed_amount):
    print("insuffiecient balance")
else:
    print(balance)