'''
2. Create a base class Animal with a method speak() that prints "Animal makes
a sound". Derive a class Dog from Animal and override the speak() method
to print "Dog barks". Instantiate the Dog class and call its speak() method.
'''

# 1. Define the base class 'Animal'
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self): 
        print("Dog barks")
   
my_dog = Dog()
my_dog.speak()
