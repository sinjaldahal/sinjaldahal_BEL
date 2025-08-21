'''
1. Define a class Student with attributes name, roll_number, and marks.
Implement a method display_info() that prints the details of the student.
Create an instance of Student and call the display_info() method to display
the student's details.
'''

class Student:
    def __init__(self , name , roll_number , marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_info(self):
        print(f"\n Name : {self.name} \n Roll No. : {self.roll_number} \n Marks : {self.marks}")

Sinjal =  Student('Sinjal Dahal', 80 ,100 )

Sinjal.display_info()
