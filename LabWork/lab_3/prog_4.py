'''
4. Write a function book_info(title, author, year) that prints book details.Call the function using
keyword arguments in different orders.
'''
def book_info(title, author, year):
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")


book_info(title="1984", author="Doraemon", year=1949)
print()
book_info(author="J.K. Rowling", year=1997, title="Harry Potter")
print()
book_info(year=1813, title="P and P", author="Jane")

