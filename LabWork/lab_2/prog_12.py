'''
**Create a dictionary to store student names as keys and 
their scores in three subjects as values (in a list). 

Write functions to:**
a. Display the average marks of each student
b. Find the topper
c. Update the marks of a student
'''



students = {
    "Bidhya": [85, 90, 78],
    "Puspha": [92, 88, 95],
    "Sher": [70, 75, 80]
}


def display_averages(student_dict):
    for name, marks in student_dict.items():
        average = sum(marks) / len(marks)
        print(f"{name}: {average:.2f}")


def find_topper(student_dict):
    topper = ""
    highest = 0
    for name in student_dict:
        avg = sum(students[name]) / len(students[name])
        if avg > highest:
            highest = avg
            topper = name
    print(f"Topper: {topper} with average {highest:.2f}")


def update_marks(student_dict):
    name = input("Enter student name: ")
    marks = input("Enter 3 marks separated by space: ").split()
    marks = [int(m) for m in marks]
    student_dict[name] = marks
    print(f"{name}'s marks updated.")

while True:
    print("\n1. Display Averages")
    print("2. Find Topper")
    print("3. Update Marks")
    print("4. Exit")
    
    ch = input("Enter your choice: ")

    if ch == '1':
        display_averages(students)
    elif ch == '2':
        find_topper(students)
    elif ch == '3':
        update_marks(students)
    elif ch == '4':
        break
    else:
        print("Invalid choice.")
