'''
 **Given two lists of integers, write a program to merge them into a single list and 
 then remove the elements that are common in both.**

'''

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8] 

list3 = list1 + list2 

print("Merged List:", list3)

list3 = set(list3)

# Remove common elements
for i in list1:
    if i in list2:
        list3.remove(i)
       

print(" after removing common elements:", list3)    