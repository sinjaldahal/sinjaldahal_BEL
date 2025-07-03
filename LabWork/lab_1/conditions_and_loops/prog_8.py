'''
Write a program that reads a number and prints whether it is a palindrome or
not.

'''

num = input("Enter a number: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")