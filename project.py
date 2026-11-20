
from abc import ABC, abstractmethod

# Tuple
SUBJECTS = ("Python", "Computer", "Mathematics")


# OOP and Abstraction
class Person(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_details(self):
        pass


# Inheritance
class Student(Person):

    def __init__(self, roll_no, name, age, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks

    # Function
    def total_marks(self):
        return sum(self.marks)

    def percentage(self):
        return self.total_marks() / len(SUBJECTS)

    def grade(self):
        percent = self.percentage()

        if percent >= 90:
            return "A+"
        elif percent >= 80:
            return "A"
        elif percent >= 70:
            return "B"
        elif percent >= 60:
            return "C"
        elif percent >= 40:
            return "D"
        else:
            return "Fail"

    def display_details(self):
        print("\n-----------------------------")
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Age:", self.age)

        for subject, mark in zip(SUBJECTS, self.marks):
            print(subject, ":", mark)

        print("Total Marks:", self.total_marks())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())
        print("-----------------------------")


# Main Management Class
class StudentManagementSystem:

    def __init__(self):
        self.students = {}
        self.roll_numbers = set()

    def get_integer(self, message, minimum=None, maximum=None):
        while True:
            try:
                value = int(input(message))

                if minimum is not None and value < minimum:
                    print("Value is too small.")
                    continue

                if maximum is not None and value > maximum:
                    print("Value is too large.")
                    continue

                return value

            except ValueError:
                print("Please enter a valid number.")

    # Add Student
    def add_student(self):

        print("\n--- Add Student ---")

        roll = self.get_integer("Enter Roll Number: ", 1)

        if roll in self.roll_numbers:
            print("Roll number already exists.")
            return

        name = input("Enter Name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        age = self.get_integer("Enter Age: ", 1, 100)

        marks = []

        for subject in SUBJECTS:
            mark = self.get_integer(
                f"Enter {subject} Marks: ", 0, 100
            )
            marks.append(mark)

        student = Student(roll, name, age, marks)

        self.students[roll] = student
        self.roll_numbers.add(roll)

        print("Student Added Successfully!")

    # Display Students
    def display_students(self):

        if not self.students:
            print("No student records found.")
            return

        for student in self.students.values():
            student.display_details()

    # Search Student
    def search_student(self):

        roll = self.get_integer("Enter Roll Number: ", 1)

        student = self.students.get(roll)

        if student is not None:
            student.display_details()
        else:
            print("Student Not Found!")

    # Update Student
    def update_student(self):

        roll = self.get_integer("Enter Roll Number: ", 1)

        student = self.students.get(roll)

        if student is None:
            print("Student Not Found!")
            return

        name = input("Enter New Name (Enter to skip): ").strip()

        if name:
            student.name = name

        age = input("Enter New Age (Enter to skip): ").strip()

        if age:
            try:
                new_age = int(age)

                if 1 <= new_age <= 100:
                    student.age = new_age
                else:
                    print("Invalid age. Old age retained.")

            except ValueError:
                print("Invalid age. Old age retained.")

        print("Student Updated Successfully!")

    # Delete Student
    def delete_student(self):

        roll = self.get_integer("Enter Roll Number: ", 1)

        if roll in self.roll_numbers:
            del self.students[roll]
            self.roll_numbers.remove(roll)

            print("Student Deleted Successfully!")

        else:
            print("Student Not Found!")

    # Class Average
    def class_average(self):

        if not self.students:
            print("No records available.")
            return

        percentages = [
            student.percentage()
            for student in self.students.values()
        ]

        average = sum(percentages) / len(percentages)

        print("Total Students:", len(percentages))
        print("Class Average:", round(average, 2), "%")

    # Main Menu
    def run(self):

        while True:

            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Class Average")
            print("7. Exit")

            choice = input("Enter Your Choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.display_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                self.class_average()

            elif choice == "7":
                print("Thank You!")
                break

            else:
                print("Invalid Choice!")


# Main Program
if __name__ == "__main__":

    app = StudentManagementSystem()
    app.run()
