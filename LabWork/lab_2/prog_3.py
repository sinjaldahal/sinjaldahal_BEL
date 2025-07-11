'''
**Create a program that reads a sentence from the user and 
stores each word as an element of a list.
Then count the frequency of each word using only lists.**

sentence = "apple apple ball cat cat dog dog dog dog";
words = sentence.split(" ")
uniq_words = set(words)
d = {}
for word in uniq_words:
    d[word] = words.count(word)

print(d)
'''

input_sentence = list(input("Enter a sentence: ").split())
print(input_sentence)
input_sentence_1 = set(input_sentence)  
word_count = {}
for i in input_sentence_1:
    word_count[i]= input_sentence.count(i)
print(word_count)
       

