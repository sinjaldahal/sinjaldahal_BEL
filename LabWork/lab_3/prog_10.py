'''
10. Given a list of temperatures in Celsius [36.5, 37.0, 39.2, 35.6, 38.7],convert them to Fahrenheit
using map(),Filter out those above 100°F using filter().
'''


temperatures_in_celsius = [36.5, 37.0, 39.2, 35.6, 38.7]
temperatures_in_fahrenheit = list(map(lambda x: (x * 9/5) + 32, temperatures_in_celsius))
filtered_temperatures = list(filter(lambda x: x <= 100, temperatures_in_fahrenheit))
print("Temperatures in Fahrenheit:", temperatures_in_fahrenheit)
print("Temperatures ≤ 100°F:", filtered_temperatures)
