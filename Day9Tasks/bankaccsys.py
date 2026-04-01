#Bank account sysytem
class Bankaccount:
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposit amount:",amount)
    def withdraw(self,amount):
        if amount<= self.balance:
            self.balance-=amount
            print("Withdraw amount:",amount)
        else:
            print("Insufficient balance")
    def display(self):
        print("Account no:",self.acc_no)
        print("Balance:",self.balance)
        
        
b=Bankaccount(101,1000)
b.deposit(500)
b.withdraw(200)
b.display()
    