'''
5. Create a function sum_numbers(*args) that accepts any number of numeric arguments and returns
their sum.Test it with 2, 3, and 5 numbers.
'''

def sum_numbers(*args):
    print(sum(args))

sum_numbers(2,4)
sum_numbers(2,4,8)
sum_numbers(5,6,8,2,9)