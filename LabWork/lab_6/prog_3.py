'''
3. Define a class BankAccount with private attributes account_number and
balance. Implement methods to deposit and withdraw money, ensuring that
the balance cannot go below zero. Provide a method to get the account
details. Test the class by performing deposit and withdrawal operations.
'''

class BankAccount:
    def __init__(self , account_number , balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self , deposit_amount):
        self.__balance += deposit_amount
        print(f"\n Your Current balance is : {self.__balance}")

    def withdraw(self , withdraw_amount):
        if (self.__balance >= withdraw_amount):
            self.__balance -= withdraw_amount
            print(f"\n Your Current balance is : {self.__balance}")

        else:
            print("\n insufficient balance !!!!!!!")

    def get_account_details(self):
        print(f"\n account number : {self.__account_number} \n balance : {self.__balance}")
    
Sinjal = BankAccount('0100', 1000)
Sinjal.withdraw(2000)
Sinjal.deposit(100000)
Sinjal.withdraw(5000)
Sinjal.get_account_details()