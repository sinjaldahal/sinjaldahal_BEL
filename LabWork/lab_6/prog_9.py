'''
9. Define a class Person with attributes name and age. Define another class
Address with attributes street, city, and zipcode. Create a Contact class that
contains an instance of Person and Address. Implement methods to display
the contact details. Create a Contact object and display its information.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

class Contact(Person, Address):
    def __init__(self, name, age, street, city, zip_code):
       
        Person.__init__(self, name, age)
        Address.__init__(self, street, city, zip_code)

    def display_info(self):
        print(f"\nName: {self.name}\nAge: {self.age}\nAddress: {self.city} / {self.street}\nZip Code: {self.zip_code}")


contact1 = Contact('Sinjal Dahal', 17, "Campus Mode", "Damak", 690069)

contact1.display_info()