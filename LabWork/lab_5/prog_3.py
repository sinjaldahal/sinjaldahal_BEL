'''
3. Create a class BankAccount with attributes account_holder,
account_number, and balance.
    ● Add methods deposit(amount) and withdraw(amount) that update the
    balance.
    ● Add a method show_balance() that prints the current balance.
    ● Create an object and perform a deposit, a withdrawal, and show the
    balance.
'''

class BankAccount:
    def __init__(self, account_holder , account_number ):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = 0

    def deposit(self,deposit):
        self.balance += deposit

    def withdraw(self,withdraw):
        if (self.balance < withdraw):
            print("Insufficient balance......")
        else:
            self.balance -= withdraw

    def show_balance(self):
        print(f"Balance : {self.balance} \n")

user_1 = BankAccount("Durga",1 )
user_1.deposit(100000000000)
user_1.withdraw(2500000)
user_1.show_balance()