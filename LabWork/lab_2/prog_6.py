'''
**Write a program to create a tuple of *n* numbers, then find:**

   a. The average of the numbers
   b. The median
   c. The mode (without using libraries)


'''


tuple_a = input("Enter the numbers separated by space: ").split()
tuple_1 = tuple(int(x) for x in tuple_a)


def average(tup):
    total = 0
    for i in tup:
        total += i
    return total / len(tup)


def median(tup):
    
    sorted_tup = list(tup)
    for i in range(len(sorted_tup)):
        for j in range(i + 1, len(sorted_tup)):
            if sorted_tup[i] > sorted_tup[j]:
                sorted_tup[i], sorted_tup[j] = sorted_tup[j], sorted_tup[i]

    n = len(sorted_tup)
    if n % 2 == 1:
        return sorted_tup[n // 2]
    else:
        mid1 = sorted_tup[n // 2 - 1]
        mid2 = sorted_tup[n // 2]
        return (mid1 + mid2) / 2


def mode(tup):
    max_count = 0
    result = tup[0]

    for i in tup:
        count = 0
        for j in tup:
            if i == j:
                count += 1
        if count > max_count:
            max_count = count
            result = i
    return result


print(f"Mean is: {average(tuple_1)}")
print(f"Median is: {median(tuple_1)}")
print(f"Mode is: {mode(tuple_1)}")
