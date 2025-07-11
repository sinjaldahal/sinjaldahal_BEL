'''
**Create a set of random numbers. Add more numbers until the set has 10 unique elements. 
Also, remove the smallest and largest element.**

'''
import random

def generate_set():
    nums = set()

    
    while len(nums) < 10:
        nums.add(random.randint(1, 100))

    print("Original Set:", nums)

    
    smallest = min(nums)
    largest = max(nums)

    
    nums.remove(smallest)
    nums.remove(largest)

    print(f"After removing smallest ({smallest}) and largest ({largest}):", nums)

generate_set()
