class Bankaccont:
    """"
    initialize account object using this properties
    """""
    def __init__(self, account_holder, account_balance=0.0):
        self.account_holder = account_holder
        self.account_balance = account_balance
    def __str__(self):
        return f'{self.account_holder} {self.account_balance}'
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"deposit amount {amount}"
                  f"account balance {self.account_balance}")
        else:
            print("amount must be positive or>0 ")

    def withdraw(self, amount):
        if amount > self.account_balance:
            self.account_balance -= amount
            print(f"withdraw amount {amount}"
                  f"account balance {self.account_balance}")
        else:
            print("insufficient funds")

    def print_balance(self):
        print(f"account balance {self.account_balance}")



name=input("enter your name")
account=Bankaccont(name)

#console program
while True:
    print("\welcome to bank account")
    print("1.deposit amount")
    print("2.withdraw amount")
    print("3.check balance")
    print("4.exit")

    choice=int(input("enter your choice"))
    if choice==1:
        amount=float(input("enter your amount"))
        account.deposit(amount)

    elif choice==2:
        amount=float(input("enter your withdraw amount"))
        account.withdraw(amount)

    elif choice==3:
        account.print_balance()

    elif choice==4:
        print("thank you")
        break

    else:
        print("invalid choice")



