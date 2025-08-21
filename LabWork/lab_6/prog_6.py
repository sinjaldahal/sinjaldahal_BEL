'''
6. Define a class Vector with attributes x and y. Overload the + operator to add
two Vector objects. Implement the __add__() method and test it by adding
two Vector instances.
'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Test the Vector class and + operator
v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(Vector.__add__(v1,v2))
result = v1 + v2
print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {result}")