class Bankaccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self.balance=balance

    def account_holder(self):
        return self.account_holder


    def balance(self):
        return self.balance

    def deposit(self,amount):
        self.balance = self.balance+amount

   def get_balance(self):
       return self.balance

   def display_balance(self):
       print(f"your balance is {self.balance}")




Account=Bankaccount(account_holder="IAN",balance=1000)
Account.deposit(100)

class SavingsAccount(Bankaccount):
    def __init__(self,account_holder,balance=100, intrest=23):
        super().__init__(account_holder,balance)
        self.intrest=intrest

    def account_holder(self):
        return self.account_holder

    def add_interest(self,interest=23):
        self.balance+=interest
        interest=interest/100
        return interest

    def get_balance(self):
        return self.balance

    def display_balance(self):
        print(f"your balance is {self.balance}")

    Account_1=Bankaccount(account_holder="IAN",balance=1000)
    Account_2=Bankaccount(account_holder="IAN",balance=1200)

print(Account.account_holder())
















