'''
Write a program to count the number of each character in a given string
using a dictionary.
'''

def print_character_positions(input_string):
    for index, char in enumerate(input_string, start=1):
        print(f"{char}:{index}", end=", " if index < len(input_string) else "")


user_input = input("Enter a string: ")
print_character_positions(user_input)