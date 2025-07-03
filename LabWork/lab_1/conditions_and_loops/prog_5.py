'''
 Write a program to find the largest and smallest number in a list entered by
the user.

'''
numbers = input("Enter numbers : ").split()
numbers = [float(num) for num in numbers]

largest = max(numbers)
smallest = min(numbers)

print("Largest number:", largest)
print("Smallest number:", smallest)