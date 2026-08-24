
class BankAccount:


    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,deposit_amount):
        self.balance+=deposit_amount
        print(f"You have depositted amount {deposit_amount} at account titled {self.account_holder}. Your current account balance is {self.balance} .")

    def withdraw(self,withdraw_amount):
        self.balance-=withdraw_amount
        print(f"You have withdraw amount {withdraw_amount} at account titled {self.account_holder}. Your current account balance is {self.balance} .")

    def show_balance(self):
        print(f"Your current account balance is Pkr {self.balance}")




class SavingsAccount(BankAccount):


    def __init__(self,account_holder,balance,interest_rate):
     super().__init__(account_holder,balance)
     self.interest_rate=interest_rate




    def add_interest(self):
         interest=(self.balance *self.interest_rate)/100
         self.balance+=interest 
         print(f"Interest added Pkr {interest}")
         print(f"Current account balance is Pkr {self.balance}")








# account=BankAccount("Ahmed Ali Malik",34500)
# account.deposit(13000)
# account.withdraw(10000)
# account.withdraw(1500)
# account.show_balance()
# account.withdraw(3500)
# account.show_balance()


account1=SavingsAccount("Ahmed Ali",50000,10)
account1.add_interest()
account1.show_balance()