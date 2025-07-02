'''
Write a Python program to remove elements from a list that are also present
in another list.

'''

list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 4, 6]

result = [item for item in list1 if item not in list2]
print("Updated list:", result)