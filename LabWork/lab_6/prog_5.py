'''
5. Define a class Person with attributes name and age. Derive a class Employee
from Person with additional attributes employee_id and salary. Implement a
method display_employee() in Employee that prints all the details. Create an
instance of Employee and display the information.
'''

class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age , employee_id , salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        print(f"\n Name : {self.name} \n Employee Id : {self.employee_id} \n Age : {self.age} \n Salary : {self.salary}")

Sinjal = Employee( name="Sinjal Dahal" , age=17 , employee_id='06969' , salary=2500000 )
Sinjal.display_employee()

