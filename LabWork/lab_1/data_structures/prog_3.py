'''
Write a Python function that accepts a list and returns a new list with only
the even numbers from the original list.

'''


numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_even_numbers(numbers):
  
    return [num for num in numbers if num % 2 == 0]
print(filter_even_numbers(numbers))