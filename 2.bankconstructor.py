class bank:
    def __init__(self):
        self.balance=0
        self.accountnumber=int(input("enter account number"))
        self.name=input("enter name")
        self.accounttype=input("enter account type")
    def display(self):
        print("name:",self.name)
        print("account number:",self.accountnumber)
        print("account type :",self.accounttype)
    def deposit(self):
        amount=int(input("enter the amount to be deposited:"))
        self.balance+=amount
        print("your account balance is:",self.balance)
    def withdraw(self):
        amount=int(input("enter the amount to withdraw"))
        if(amount>self.balance):
            print(" insufficient balance")
        else:
            self.balance-=amount
            print("your account balance is:",self.balance)
account=bank()
account.display()
account.deposit()
account.withdraw()
