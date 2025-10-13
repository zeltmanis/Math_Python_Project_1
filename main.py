import csv
import os

FILENAME = 'students.csv'


def load_students():
    students = []
    try:
        with open(FILENAME, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        print("No students.csv file found. A new one will be created when a student is added.")
    return students


def save_students(students):
    with open(FILENAME, 'w', newline='') as csvfile:
        fieldnames = ['name', 'age', 'gender', 'country']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)


def review_students(students):
    if not students:
        print("No students to show.")
        return
    print("\n--- Student List ---")
    for i, student in enumerate(students, start=1):
        print(
            f"{i}. Name: {student['name']}, Age: {student['age']}, Gender: {student['gender']}, Country: {student['country']}")
    print("--------------------\n")


def add_student():
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

    # Check if file exists
    file_exists = os.path.isfile(FILENAME)

    with open(FILENAME, 'a', newline='') as csvfile:
        fieldnames = ['name', 'age', 'gender', 'country']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists or os.path.getsize(FILENAME) == 0:
            writer.writeheader()

        writer.writerow(new_student)

    print(f"Student {name} added successfully!\n")


def delete_student():
    students = load_students()
    if not students:
        print("No students to delete.")
        return

    review_students(students)
    try:
        choice = int(input("Enter the number of the student to delete: "))
        if 1 <= choice <= len(students):
            removed = students.pop(choice - 1)
            save_students(students)
            print(f"Student {removed['name']} has been deleted.\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def match_students(students):
    print("\n--- Match Students ---")
    print("Basic compatibility: same country and age difference ≤ 2 years.\n")

    matched = []
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            s1 = students[i]
            s2 = students[j]
            if s1['country'] == s2['country']:
                age_diff = abs(int(s1['age']) - int(s2['age']))
                if age_diff <= 2:
                    matched.append((s1['name'], s2['name']))

    if matched:
        print("Matched Pairs:")
        for pair in matched:
            print(f" - {pair[0]} & {pair[1]}")
    else:
        print("No compatible matches found.")
    print("----------------------\n")


def main():
    while True:
        print("What would you like to do?")
        print("1. Review students")
        print("2. Add new student")
        print("3. Match students by compatibility")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            students = load_students()
            review_students(students)
        elif choice == '2':
            add_student()
        elif choice == '3':
            students = load_students()
            match_students(students)
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
