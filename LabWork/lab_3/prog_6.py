'''
6. Write a function student_profile(**kwargs) that prints the key-value pairs passed (e.g., name, age,
grade). Call it with at least three named arguments.
'''

def student_profile(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

student_profile(name="Sinjal",age=10,marks=56)
student_profile(name="Ram",age=20,marks=96)
student_profile(name="Shyam",age=30,marks=26)
