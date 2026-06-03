import copy

try:
    n = int(input("Enter number of students: "))
    if n <= 0:
        raise ValueError("Number of students must be positive.")

    names = []
    roll_numbers = []
    marks_list = []

    for i in range(n):
        print(f"\nStudent {i+1}") # Display student number
        name = input("Enter Name: ")
        roll = int(input("Enter Roll Number: "))
        marks = []

        for j in range(3):
            mark = int(input(f"Enter Subject {j+1} Mark: "))
            marks.append(mark)

        names.append(name)
        roll_numbers.append(roll)
        marks_list.append(marks)

    print("\n----- Lists -----")
    print("Names:", names)
    print("Roll Numbers:", roll_numbers)
    print("Marks:", marks_list)

    student_dict = dict(zip(roll_numbers, names))

    print("\nDictionary using zip():")
    print(student_dict)
    print("\n----- String Operations -----")

    upper_names = [name.upper() for name in names]

    print("Uppercase Names:", upper_names)
    long_names = [
        name for name in names
        if len(name) > 5
    ]
    print("Names longer than 5 characters:",long_names)
    count_a = sum(
        1 for name in names
        if name.upper().startswith("A")
    )
    print("Names starting with A:",count_a)
    print("\n----- List Comprehension -----")
    avg_above_75 = [    # List comprehension to get names of students with average marks > 75

        names[i]

        for i in range(len(names))

        if sum(marks_list[i]) / 3 > 75
    ]
    print("Students with average > 75:",avg_above_75)
    even_rolls = [

        roll

        for roll in roll_numbers

        if roll % 2 == 0
    ]
    print("Even Roll Numbers:",even_rolls)
    print("\n----- Tuple -----")
    first_student_marks = tuple(marks_list[0])
    print("First Student Marks Tuple:",first_student_marks)
    print("\n----- Set -----")
    unique_marks = {    # Set comprehension to get unique
        mark
        for student_marks in marks_list
        for mark in student_marks
    }

    print("Unique Marks:", unique_marks)
    print("\n----- Shallow Copy -----")

    shallow_copy = copy.copy(marks_list)
    print(shallow_copy)

    print("\n----- Deep Copy -----")
    deep_copy = copy.deepcopy(marks_list)
    print(deep_copy)

    print("\nModifying original marks...")  # Modifying original marks to show effect on copies
    marks_list[0][0] = 999

    print("\nOriginal Marks List:")
    print(marks_list)
    
    print("\nShallow Copy:")
    print(shallow_copy)
    
    print("\nDeep Copy:")
    print(deep_copy)

except ValueError as e:
    print("Input Error:", e)
except Exception as e:
    print("Unexpected Error:", e)