'''
Write a program to input key-value pairs from the user and store them in a
dictionary. Allow the user to search for a key and display its value.

'''

data = {}
n = int(input("How many key-value pairs do you want to enter? "))
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

search_key = input("Enter key to search: ")
if search_key in data:
    print(f"Value: {data[search_key]}")
else:
    print("Key not found.")