'''
 Write a program that accepts 10 integers from the user and counts how many
are positive, negative, and zero.

'''

positive_count = 0
negative_count = 0
zero_count = 0

for i in range(10):
    num = int(input(f"Enter integer #{i+1}: "))
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Zeros:", zero_count)