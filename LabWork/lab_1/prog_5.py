'''
Create a set of prime numbers less than 50. Write a program to check
whether a given number exists in the set or not.

'''
primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}

num = int(input("Enter a number: "))
if num in primes:
    print(f"{num} is a prime number less than 50.")
else:
    print(f"{num} is not a prime number less than 50.")