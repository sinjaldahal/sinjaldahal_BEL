'''
7. Create a class Book with attributes title and author. Overload the __str__()
method to return a string representation of the Book object in the format
"Title by Author". Test this method by printing a Book instance.
'''

class Book:
    def __init__(self , title , author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
book1 = Book(title="Mahabharat" , author="Ved Vyasa")
print(book1)