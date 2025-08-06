'''
1. Create a class Book with attributes title, author, and price. Write a
constructor to initialize these values and create an object with sample data.
● Add a method display_info() to the Book class that prints the book's
title, author, and price. Call this method using a Book object.
● Add a method update_price(new_price) to the Book class that updates
the book's price. Demonstrate how to use it with an object.

'''
 
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print("Title \t\t Author \t\t price \n ")
        print(f"{self.title} \t\t {self.author} \t\t {self.price}\n")

    def update_price(self,new_price):
        self.price = new_price

book1 = Book("Maths","dr Dahal",1069)
book1.display_info()
book1.update_price(500)
book1.display_info()