'''
9. Given a list [10, 15, 20, 25, 30], use filter() and a lambda function to extract numbers divisible by
   10.
'''
list1 = [10, 15, 20, 25, 30]
divisible_by_ten = list(filter(lambda x : x%10 == 0,list1))
print(divisible_by_ten)

