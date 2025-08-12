'''
Project 1
Create a CLI (Command Line Interface) contact book that allows users to:
● Add a new contact (append to file)
● View all contacts (read from file)
● Search for a contact (read and filter)
● Handle file-related exceptions (e.g., file not found)
File Used:
contacts.txt (stores contact info: Name, Phone)
'''

import os
directory = r"C:\Users\daSynZyoll SIR\Desktop\sinjaldahal_BEL-main\sinjaldahal_BEL-main\LabWork\lab_4\project_1"

filename = "contacts.txt"

file_path = os.path.join(directory, filename)

contacts = []
print("1. New Contacts \n 2. View Contacts \n 3. Search Contacts")
choice = input("Enter a choice (1, 2, 3): ")


def new_contacts(contacts,name,number):
    name = input("Enter Name: ")
    number = input("Enter Phone Number:")
    contacts_add = {"name" : name , "phone_number" : number }
    
    with open(file_path,"a") as file:
        file.write(str(contacts_add) + "\n ")

    file.close()

def view_contacts():
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())
    file.close()

def search_contacts():
    name_input = input("Enter Name: ")
    with open(file_path,"r") as file:
        for line in file:
            if(name_input in line):
                print(line, end="")
                found = True
        if not found:
            print("Name not found !!!")

match choice:
    case "1":
        new_contacts(contacts,name="person",number="0000000000")
    case "2":
        view_contacts()
    case "3":
        search_contacts()
    case _:
        print("Invalid choice.")
