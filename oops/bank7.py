# create bank class with accncrtn as constructor and deposit and withdraw as methods

# accountcreation   acno   #as constructor


# deposit    amount
# withdraw   amount

class Bank:
    bank_name="SBI"

    def __init__(self,accno):
        self.accno=accno
        self.balance=0
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("Your",Bank.bank_name,"account credited with amount",self.amount)
        print("Available balance is",self.balance)
    def withdraw(self,amnt):
        self.amnt=amnt
        if self.amnt>self.balance:
            print("insufficient balance")
        else:
            self.balance=self.balance-self.amnt
            print("your",Bank.bank_name,"has been debited with amount",self.amnt)
            print("the available balance is",self.balance)

acc1=Bank(12345)
acc1.withdraw(5000)
acc1.deposit(75000)
acc1.deposit(5000)
acc1.withdraw(35000)




