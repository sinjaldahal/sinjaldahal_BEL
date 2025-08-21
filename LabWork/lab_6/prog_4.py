'''
4. Create a base class Shape with a method area(). Derive two classes
Rectangle and Circle from Shape. Implement the area() method in both
derived classes. Instantiate Rectangle and Circle, and demonstrate
polymorphism by calling their area() methods.
'''
import math
class Shape:
    def __init__(self):
        pass
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self , length , breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return f"{self.length*self.breadth}"

class Circle(Shape):
    def __init__(self , radius):
        self.radius = radius
    def area(self):
        return f"{math.pi*(math.pow(self.radius,2))}"

rectangle1 = Rectangle(12,2)
circle1 = Circle(4)

shapes = [rectangle1 , circle1]

for shape in shapes:
    print(f"Object of type: {type(shape).__name__}")
    print(f"Area: {shape.area()}\n")