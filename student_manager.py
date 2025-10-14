import csv
import os

FILENAME = 'students.csv'

class StudentManager:
    def __init__(self, filename=FILENAME):
        self.filename = filename
        self.students = self.load_students()
        self.next_id = self.get_next_id()

    def get_next_id(self):
        if not self.students:
            return 1
        max_id = max(int(student['id']) for student in self.students)
        return max_id + 1

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
        fieldnames = ['id', 'name', 'age', 'gender', 'country', 'studies', 'sports', 'art', 'games']
        with open(self.filename, 'w', newline='') as csvfile:
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
            print(f"{i}. ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Gender: {student['gender']}, "
                  f"Country: {student['country']}, Studies: {student['studies']}, Sports: {student['sports']}, "
                  f"Art: {student['art']}, Games: {student['games']}")
        print("--------------------\n")

    def add_student(self):
        print("\n--- Add New Student ---")
        name = input("Enter name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        country = input("Enter country: ")
        studies = input(
            "Enter study program (Software Development, Cyber Security, AI, Digital Industrial Engineering): ")

        def ask_interest(prompt):
            while True:
                print(f"{prompt}")
                print("1. Yes")
                print("2. No")
                choice = input("Enter choice (1 or 2): ").strip()
                if choice == '1':
                    return 'yes'
                elif choice == '2':
                    return 'no'
                else:
                    print("Please enter 1 or 2.")

        sports = ask_interest("Interested in sports?")
        art = ask_interest("Interested in art?")
        games = ask_interest("Interested in video games?")

        new_student = {
            'id': str(self.next_id),
            'name': name,
            'age': age,
            'gender': gender,
            'country': country,
            'studies': studies,
            'sports': sports,
            'art': art,
            'games': games
        }

        self.students.append(new_student)
        self.next_id += 1
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