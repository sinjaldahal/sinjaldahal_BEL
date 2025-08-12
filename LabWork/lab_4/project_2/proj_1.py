'''
Project 2
Create a simple banking system that:
● Stores customer info in a file
● Allows deposits and withdrawals using functions
● Updates customer balance
● Logs all transactions in a separate file
● Handles exceptions gracefully
Files Used:
customers.txt — stores customer records in the format:
Name,AccountNumber,Balance
transactions.txt — appends every deposit or withdrawal record with timestamp
'''

import os
from datetime import datetime
folder = r"C:\Users\daSynZyoll SIR\Desktop\sinjaldahal_BEL-main\sinjaldahal_BEL-main\LabWork\lab_4\project_2"
os.makedirs(folder, exist_ok=True)

customer_file = os.path.join(folder, "customer_info.txt")
transaction_file = os.path.join(folder, "transactions.txt")

def load_customers():
    customers = {}
    if not os.path.exists(customer_file):
        return customers
    with open(customer_file, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(",")
                if len(parts) == 3:
                    name, acc_num, balance = parts
                    customers[acc_num] = {"name": name, "balance": float(balance)}
    return customers

def save_customers(customers):
    with open(customer_file, "w") as f:
        for acc_num, info in customers.items():
            f.write(f"{info['name']},{acc_num},{info['balance']}\n")

def log_transaction(acc_num, type_, amount):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(transaction_file, "a") as f:
        f.write(f"{time},{acc_num},{type_},{amount}\n")

def add_customer(customers, name, acc_num, balance=0):
    if acc_num in customers:
        print("This account number already exists.")
        return
    customers[acc_num] = {"name": name, "balance": float(balance)}
    save_customers(customers)
    print(f"Customer {name} added with account {acc_num}.")

def deposit(customers, acc_num, amount):
    if amount <= 0:
        print("Enter a positive amount.")
        return
    if acc_num not in customers:
        print("Account not found.")
        return
    customers[acc_num]["balance"] += amount
    save_customers(customers)
    log_transaction(acc_num, "DEPOSIT", amount)
    print(f"Deposited {amount}. New balance: {customers[acc_num]['balance']}")

def withdraw(customers, acc_num, amount):
    if amount <= 0:
        print("Enter a positive amount.")
        return
    if acc_num not in customers:
        print("Account not found.")
        return
    if customers[acc_num]["balance"] < amount:
        print("Not enough balance.")
        return
    customers[acc_num]["balance"] -= amount
    save_customers(customers)
    log_transaction(acc_num, "WITHDRAW", amount)
    print(f"Withdrew {amount}. New balance: {customers[acc_num]['balance']}")

def show_balance(customers, acc_num):
    if acc_num in customers:
        print(f"Name: {customers[acc_num]['name']}")
        print(f"Balance: {customers[acc_num]['balance']}")
    else:
        print("Account not found.")

customers = load_customers()
add_customer(customers, "Sinjal", "1010", 500)
deposit(customers, "1010", 200)
withdraw(customers, "1010", 100)
show_balance(customers, "1010")
