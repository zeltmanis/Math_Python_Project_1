import csv

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


def review_students(students):
    if not students:
        print("No students to show.")
        return
    print("\n--- Student List ---")
    for student in students:
        print(
            f"Name: {student['name']}, Age: {student['age']}, Gender: {student['gender']}, Country: {student['country']}")
    print("--------------------\n")


def add_student():
    print("\n--- Add New Student ---")
    name = input("Enter name: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    country = input("Enter country: ")

    # Save to CSV
    with open(FILENAME, 'a', newline='') as csvfile:
        fieldnames = ['name', 'age', 'gender', 'country']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if file is empty and write headers if needed
        try:
            with open(FILENAME, 'r') as checkfile:
                if not checkfile.read(1):
                    writer.writeheader()
        except FileNotFoundError:
            writer.writeheader()

        writer.writerow({
            'name': name,
            'age': age,
            'gender': gender,
            'country': country
        })

    print(f"Student {name} added successfully!\n")


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
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            students = load_students()
            review_students(students)
        elif choice == '2':
            add_student()
        elif choice == '3':
            students = load_students()
            match_students(students)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()