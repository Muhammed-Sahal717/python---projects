students = []


# Add Student
def add_student():

    name = input("Enter student name: ")

    found = False

    for s in students:

        if s["name"] == name:
            found = True

    if found == True:

        print("Student already exists")

    else:

        marks = int(input("Enter marks: "))

        students.append({
            "name": name,
            "marks": marks
        })

        print("Student added successfully")


# View Students
def view_students():

    if len(students) == 0:

        print("No students found")

    else:

        print("\n------ Student List ------")

        for s in students:

            print("Name  :", s["name"])
            print("Marks :", s["marks"])

            print("--------------------------")


# Search Student
def search_student():

    name = input("Enter student name to search: ")

    found = False

    for s in students:

        if s["name"] == name:

            print("Student found")
            print("Marks =", s["marks"])

            found = True

            break

    if found == False:

        print("Student not found")


# Delete Student
def delete_student():

    name = input("Enter student name to delete: ")

    found = False

    for s in students:

        if s["name"] == name:

            students.remove(s)

            print("Student deleted successfully")

            found = True

            break

    if found == False:

        print("Student not found")


# Update Marks
def update_marks():

    name = input("Enter student name: ")

    found = False

    for s in students:

        if s["name"] == name:

            new_marks = int(input("Enter new marks: "))

            s["marks"] = new_marks

            print("Marks updated successfully")

            found = True

            break

    if found == False:

        print("Student not found")


# Average Marks
def average_marks():

    if len(students) == 0:

        print("No students available")

    else:

        total = 0

        for s in students:

            total = total + s["marks"]

        average = total / len(students)

        print("Average Marks =", average)


# Main Menu
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Marks")
    print("6. Average Marks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        search_student()

    elif choice == "4":

        delete_student()

    elif choice == "5":

        update_marks()

    elif choice == "6":

        average_marks()

    elif choice == "7":

        print("Program Ended")

        break

    else:

        print("Invalid choice")