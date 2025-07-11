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


max_num = input_list[0]
min_num = input_list[0]

for i in range(1, n):
    if input_list[i] > max_num:
        max_num = input_list[i]
    if input_list[i] < min_num:
        min_num = input_list[i]

print("Maximum number:", max_num)
print("Minimum number:", min_num)


sorted_list = input_list[:] 
for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_list[j] > sorted_list[j + 1]:
            # Swap
            temp = sorted_list[j]
            sorted_list[j] = sorted_list[j + 1]
            sorted_list[j + 1] = temp

print("Sorted List in Ascending Order:", sorted_list)


unique_list = []
for i in range(n):
    is_duplicate = False
    for j in range(len(unique_list)):
        if input_list[i] == unique_list[j]:
            is_duplicate = True
            break
    if not is_duplicate:
        unique_list.append(input_list[i])

print("List without duplicates:", unique_list)
