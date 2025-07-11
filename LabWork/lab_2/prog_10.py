'''
**Write a Python function that accepts a sentence and
 returns a set of all unique vowels used.**

'''

sentence = input("Enter a sentence: ")

vowels = 'aeiou'
unique_vowels = []

for ch in sentence.lower():
    if ch in vowels and ch not in unique_vowels:
        unique_vowels.append(ch)

print("Unique vowels in the sentence:", set(unique_vowels))
