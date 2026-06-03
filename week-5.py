from abc import ABC, abstractmethod

# ---------------- ABSTRACT CLASS ----------------
class Evaluation(ABC):

    @abstractmethod
    def calculate_grade(self):
        pass

# ---------------- PERSON CLASS ----------------
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

# ---------------- STUDENT CLASS ----------------
class Student(Person, Evaluation):

    student_count = 0

    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)

        self.roll_no = roll_no
        self.marks = marks

        Student.student_count += 1

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / 3

    def calculate_grade(self):

        avg = self.average_marks()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "D"

    def display(self):
        print("\nName:", self.get_name())
        print("Age:", self.get_age())
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("Total:", self.total_marks())
        print("Average:", round(self.average_marks(), 2))
        print("Grade:", self.calculate_grade())

    def __lt__(self, other):
        return self.total_marks() > other.total_marks()

    @staticmethod
    def validate_marks(mark):
        return 0 <= mark <= 100

    @classmethod
    def show_count(cls):
        print("\nTotal Students:", cls.student_count)

# ---------------- SPORTS CLASS ----------------
class Sports:
    def __init__(self, sports_score):
        self.sports_score = sports_score

    def display_sports(self):
        print("Sports Score:", self.sports_score)

# ---------------- RESULT CLASS ----------------
class Result(Student, Sports):
    def __init__(
            self,
            name,
            age,
            roll_no,
            marks,
            sports_score
    ):

        Student.__init__(
            self,
            name,
            age,
            roll_no,
            marks
        )

        Sports.__init__(
            self,
            sports_score
        )

    def final_total(self):
        return self.total_marks() + self.sports_score

    def display(self):
        super().display()

        print("Sports Score:", self.sports_score)
        print("Final Score:", self.final_total())

# ---------------- MAIN ----------------
students = []

try:
    n = int(input("Enter number of students: "))
    for i in range(n):
        print("\nStudent", i + 1)
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        roll_no = int(
            input("Enter Roll Number: ")
        )

        marks = []

        for j in range(3):
            mark = int(input(f"Enter Mark {j+1}: "))

            if not Student.validate_marks(mark):
                raise ValueError("Marks must be between 0 and 100")

            marks.append(mark)

        sports_score = int(input("Enter Sports Score: "))

        student = Result(
            name,
            age,
            roll_no,
            marks,
            sports_score
        )

        students.append(student)

    students.sort()

    print("\n========== RANK LIST ==========")
    rank = 1

    for student in students:
        print("\nRank:", rank)
        student.display()
        rank += 1
    Student.show_count()

except ValueError as e:
    print("Error:", e)
except Exception as e:

    print("Unexpected Error:", e)