'''
Given a list of names, write a program to count how many times each name
appears using a dictionary.

'''

names = ['Sinjal', 'Sher', 'Sher', 'Sher', 'Pushpa', 'Sinjal']
name_counts = {}

for name in names:
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1

print(name_counts)