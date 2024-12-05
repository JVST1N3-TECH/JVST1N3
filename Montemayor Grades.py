
grades = {}

def view_students():
    if grades:
        print("Student Grades List:")
        for name, subjects in grades.items():
            print(f"Student: {name}")
            for subject, grade in subjects.items():
                print(f"  Subject: {subject}, Grade: {grade}")
    else:
        print("No student records found.")

def add_or_update_student(name, subject, grade):
    if name not in grades:
        grades[name] = {}
        print(f"Adding new student '{name}' with subject '{subject}' and grade '{grade}'.")
    else:
        print(f"Updating student '{name}' with subject '{subject}' to grade '{grade}'.")
    
    grades[name][subject] = grade

def view_specific_student(name):
    if name in grades:
        print(f"Student: {name}")
        for subject, grade in grades[name].items():
            print(f"  Subject: {subject}, Grade: {grade}")
    else:
        print(f"Student '{name}' not found.")

def delete_student(name):
    if name in grades:
        del grades[name]
        print(f"Student '{name}' deleted.")
    else:
        print(f"Student '{name}' not found.")

# Main loop
while True:
    print("---Student Grades---")
    print("\n1. View All Student Grades")
    print("2. Add or Update Student Grade")
    print("3. View Specific Student Grades")
    print("4. Delete Student Grade")
    print("5. Exit")
    
    choice = input("choose an option (1-5):")

    if choice == '1':
        view_students()
    elif choice == '2':
        name = input("Enter student name: ")
        subject = input("Enter subject: ")
        grade = input("Enter grade: ")
        add_or_update_student(name, subject, grade)
    elif choice == '3':
        name = input("Enter name of the student to view: ")
        view_specific_student(name)
    elif choice == '4':
        name = input("Enter name of the student to delete: ")
        delete_student(name)
    elif choice == '5':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice, please try again.")