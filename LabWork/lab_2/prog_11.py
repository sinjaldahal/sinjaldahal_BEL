'''
**Given a list of numbers with duplicates, use a set to remove the duplicates. 
Then, convert it back to a sorted list and display the result.**

'''

numbers = input("Enter numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]

unique_sorted = sorted(set(numbers))

print("Sorted list without duplicates:", unique_sorted)
