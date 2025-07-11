'''
**Write a Python function that accepts a list and returns a new list containing only the elements at even indexes 
and those that are prime numbers.**

l = [2,3,4,5,6,7,8,9]
even_indices = range(0,len(l),2)
print(even_indices)

for index in even_indices:
    count = 0
    for i in range(1,l[index]+1):
        if (l[index]%i==0):
            count +=1
    if count==2:
        print(l[index])

        
'''

def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count == 2

def primes_at_even_indices(lst):
    result = []
    even_indices = range(0, len(lst), 2)

    for index in even_indices:
        if is_prime(lst[index]):
            result.append(lst[index])
    return result


l = input("Enter a list of numbers separated by spaces: ").split()
l = [int(x) for x in l]  

filtered = primes_at_even_indices(l)
print("Prime numbers at even indices:", filtered)
