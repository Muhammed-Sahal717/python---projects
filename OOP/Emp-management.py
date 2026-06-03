from abc import ABC, abstractmethod


class EmployeeNotFoundError(Exception):
    pass


class InvalidSalaryError(Exception):
    pass


class Person(ABC):
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def display(self):
        pass


class Employee(Person):
    employee_count = 0

    def __init__(self, emp_id, name, salary):
        super().__init__(emp_id, name) 
        self.set_salary(salary)
        Employee.employee_count += 1

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary < 0:
            raise InvalidSalaryError("Salary cannot be negative.")

        self.__salary = salary

    def display(self):
        print("\nEmployee Details")
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.__salary)

    def __gt__(self, other):
        return self.get_salary() > other.get_salary()

    @classmethod
    def show_count(cls):
        print("\nTotal Employees:", cls.employee_count)

    @staticmethod
    def company_policy():
        print("\nOffice starts at 9 AM and ends at 5 PM.")


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Employee Salary: "))
        emp = Employee(emp_id, name, salary)
        self.employees.append(emp)
        print("Employee added successfully!")

    def view_employees(self):
        if len(self.employees) == 0:
            print("No employees found.")
            return

        for emp in self.employees:
            emp.display()

        Employee.show_count()

    def update_salary(self):
        emp_id = input("Enter Employee ID: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:
                new_salary = float(input("Enter New Salary: "))
                emp.set_salary(new_salary)
                print("Salary updated successfully!")
                return

        raise EmployeeNotFoundError("Employee not found.")

    def search_employee(self):
        emp_id = input("Enter Employee ID: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.display()
                return

        raise EmployeeNotFoundError("Employee not found.")

    def delete_employee(self):
        emp_id = input("Enter Employee ID: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                Employee.employee_count -= 1
                print("Employee deleted successfully!")
                return

        raise EmployeeNotFoundError("Employee not found.")

    def highest_paid_employee(self):
        if len(self.employees) == 0:
            print("No employees found.")
            return

        highest = self.employees[0]

        for emp in self.employees:
            if emp > highest:
                highest = emp

        print("\nHighest Paid Employee")
        highest.display()


system = EmployeeManagementSystem()

while True:
    try:
        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Salary")
        print("4. Search Employee")
        print("5. Delete Employee")
        print("6. Company Policy")
        print("7. Highest Paid Employee")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.add_employee()
        elif choice == "2":
            system.view_employees()
        elif choice == "3":
            system.update_salary()
        elif choice == "4":
            system.search_employee()
        elif choice == "5":
            system.delete_employee()
        elif choice == "6":
            Employee.company_policy()
        elif choice == "7":
            system.highest_paid_employee()
        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice.")

    except EmployeeNotFoundError as e:
        print(e)
    except InvalidSalaryError as e:
        print(e)
    except ValueError:
        print("Please enter valid numeric values.")
    except Exception as e:
        print("Unexpected Error:", e)