'''
2. Create a class Student with attributes name and marks. Create three objects
of the class and display their details using a method show_details().

'''

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        print(f"Name : {self.name} \t\t Marks : {self.marks} \n")

roll_1 = Student("Ram",96)
roll_2 = Student("Shyam",69)
roll_3 = Student("Hari",76)

roll_1.show_details()
roll_2.show_details()
roll_3.show_details()