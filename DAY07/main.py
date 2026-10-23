
import json

# File name for storing student records
FILE_NAME = "students.json"


# Load students from JSON file
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

            if isinstance(data, dict):
                return data

            print("Invalid student data format!")
            return {}

    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        print("Error: students.json contains invalid JSON!")
        return {}


# Load saved students when program starts
students = load_students()


# Save students to JSON file
def save_students():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)

        print("Students Saved Successfully!")

    except OSError as error:
        print("Error saving students:", error)


# Get valid marks from user
def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter Student Marks (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100!")

        except ValueError:
            print("Invalid input! Please enter a number.")


# Add Student
def add_student():
    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty!")
        return

    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Student name cannot be empty!")
        return

    marks = get_valid_marks()

    students[student_id] = {
        "name": name,
        "marks": marks
    }

    save_students()
    print("Student Added Successfully!")


# View All Students
def view_students():
    if not students:
        print("No Students Found!")
        return

    print("\n===== ALL STUDENTS =====")

    for student_id, info in students.items():
        print("Student ID:", student_id)
        print("Name:", info["name"])
        print("Marks:", info["marks"])
        print("--------------------")


# Search Student
def search_student():
    student_id = input("Enter Student ID to Search: ").strip()

    if student_id in students:
        print("\n===== STUDENT FOUND =====")
        print("Student ID:", student_id)
        print("Name:", students[student_id]["name"])
        print("Marks:", students[student_id]["marks"])

    else:
        print("Student Not Found!")


# Update Student Marks
def update_student():
    student_id = input("Enter Student ID to Update: ").strip()

    if student_id in students:
        print("Student Name:", students[student_id]["name"])
        print("Current Marks:", students[student_id]["marks"])

        new_marks = get_valid_marks()

        students[student_id]["marks"] = new_marks

        save_students()
        print("Student Marks Updated Successfully!")

    else:
        print("Student Not Found!")


# Delete Student
def delete_student():
    student_id = input("Enter Student ID to Delete: ").strip()

    if student_id in students:
        print("Student Name:", students[student_id]["name"])

        confirm = input("Are you sure? (yes/no): ").strip().lower()

        if confirm == "yes":
            students.pop(student_id)

            save_students()
            print("Student Deleted Successfully!")

        else:
            print("Deletion Cancelled!")

    else:
        print("Student Not Found!")


# Main Menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Save Students to File")
    print("7. Exit")

    choice = input("Enter Your Choice: ").strip()

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        save_students()

    elif choice == "7":
        print("Thank you! Program Closed.")
        break

    else:
        print("Invalid Choice! Please select 1 to 7.")
