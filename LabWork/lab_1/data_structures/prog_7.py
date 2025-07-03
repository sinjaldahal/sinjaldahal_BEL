'''
Write a Python program to merge two dictionaries and sum the values of
common keys.

'''
def merge_and_sum(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged


dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}
result = merge_and_sum(dict1, dict2)
print(result)