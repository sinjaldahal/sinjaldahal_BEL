'''
Design and implement a Student Report Card Management System using Python that allows a teacher to:

* Add new student records (name, roll number, subject-wise marks)
* View the report of all students
* Display the topper(s) of the class based on average marks
* Search for a student by roll number
* Display all students who have failed in one or more subjects
* Optionally update marks of any student

'''



students = {} 


def add_student():
    name = input("Enter student's name: ")
    roll = input("Enter roll number: ")
    marks = []
    subjects = int(input("Enter number of subjects: "))
    
    for i in range(subjects):
        mark = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    students[roll] = {
        "name": name,
        "marks": marks
    }
    print("Student added successfully!")



def view_all():
    if not students:
        print("No student records found.")
        return
    for roll, data in students.items():
        print(f"\nRoll No: {roll}")
        print(f"Name: {data['name']}")
        print(f"Marks: {data['marks']}")
        avg = sum(data["marks"]) / len(data["marks"])
        print(f"Average: {avg:.2f}")



def find_topper():
    if not students:
        print("No student records to evaluate.")
        return

    max_avg = -1
    toppers = []

    for roll, data in students.items():
        avg = sum(data["marks"]) / len(data["marks"])
        if avg > max_avg:
            max_avg = avg
            toppers = [data["name"]]
        elif avg == max_avg:
            toppers.append(data["name"])

    print(f"Topper with average {max_avg:.2f}: {', '.join(toppers)}")



def search_student():
    roll = input("Enter roll number to search: ")
    if roll in students:
        data = students[roll]
        print(f"Name: {data['name']}")
        print(f"Marks: {data['marks']}")
        avg = sum(data["marks"]) / len(data["marks"])
        print(f"Average: {avg:.2f}")
    else:
        print("Student not found.")



def failed_students():
    print("\nStudents who failed in one or more subjects:")
    found = False
    for roll, data in students.items():
        if any(m < 35 for m in data["marks"]):
            print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}")
            found = True
    if not found:
        print("No student has failed.")



def update_marks():
    roll = input("Enter roll number of student to update marks: ")
    if roll in students:
        new_marks = []
        subjects = len(students[roll]["marks"])
        for i in range(subjects):
            mark = int(input(f"Enter new marks for subject {i+1}: "))
            new_marks.append(mark)
        students[roll]["marks"] = new_marks
        print("Marks updated successfully.")
    else:
        print("Student not found.")



while True:
    print("\n=== Student Report Card System ===")
    print("1. Add Student Record")
    print("2. View All Reports")
    print("3. Find Topper")
    print("4. Search by Roll Number")
    print("5. Show Failed Students")
    print("6. Update Marks")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_all()
    elif choice == '3':
        find_topper()
    elif choice == '4':
        search_student()
    elif choice == '5':
        failed_students()
    elif choice == '6':
        update_marks()
    elif choice == '7':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
