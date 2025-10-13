import csv
import os

FILENAME = 'students.csv'

class StudentManager:
    def __init__(self, filename=FILENAME):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        students = []
        try:
            with open(self.filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    students.append(row)
        except FileNotFoundError:
            pass  # File will be created later
        return students

    def save_students(self):
        with open(self.filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'age', 'gender', 'country']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in self.students:
                writer.writerow(student)

    def review_students(self):
        if not self.students:
            print("No students to show.")
            return
        print("\n--- Student List ---")
        for i, student in enumerate(self.students, start=1):
            print(f"{i}. Name: {student['name']}, Age: {student['age']}, Gender: {student['gender']}, Country: {student['country']}")
        print("--------------------\n")

    def add_student(self):
        print("\n--- Add New Student ---")
        name = input("Enter name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        country = input("Enter country: ")

        new_student = {
            'name': name,
            'age': age,
            'gender': gender,
            'country': country
        }

        self.students.append(new_student)
        self.save_students()
        print(f"Student {name} added successfully!\n")

    def delete_student(self):
        if not self.students:
            print("No students to delete.")
            return

        self.review_students()
        try:
            choice = int(input("Enter the number of the student to delete: "))
            if 1 <= choice <= len(self.students):
                removed = self.students.pop(choice - 1)
                self.save_students()
                print(f"Student {removed['name']} has been deleted.\n")
            else:
                print("Invalid number.\n")
        except ValueError:
            print("Please enter a valid number.\n")