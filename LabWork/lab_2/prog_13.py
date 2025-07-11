'''
**Write a program that reads a text and
 counts the frequency of each character 
 (excluding spaces and special characters) using a dictionary.**

'''

text = input("Enter a text: ")

frequency = {}

for char in text:
     
    char = char.lower() 
    if char in frequency:
            frequency[char] += 1
    else:
            frequency[char] = 1


print("\nCharacter Frequencies:")
for char, count in frequency.items():
    print(f"{char}: {count}")
