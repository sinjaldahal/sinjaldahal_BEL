'''
**Write a program to input *n* numbers and store them in a list. Then perform the following operations:**

   i) Using built-in functions
   ii) Without using built-in functions
   a. Find the maximum and minimum number
   b. Sort the list in ascending order
   c. Remove duplicate elements


'''

n = int(input("Enter the number of elements: "))
input_list = []

for i in range(n):
    val = int(input(f"Enter element {i + 1}: "))
    input_list.append(val)

print("Input List:", input_list)


max_num = max(input_list)
min_num = min(input_list)

print("Maximum number:", max_num)
print("Minimum number:", min_num)

sorted_list = sorted(input_list)
print("Sorted List in Ascending Order:", sorted_list)


unique_list = list(set(input_list))
unique_list.sort()  
print("List without duplicates:", unique_list)
