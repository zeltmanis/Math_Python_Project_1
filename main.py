from student_manager import StudentManager
from matchmaker import MatchMaker

def main():
    manager = StudentManager()  # Handles loading, saving, adding, deleting

    while True:
        print("\nWhat would you like to do?")
        print("1. Review students")
        print("2. Add new student")
        print("3. Match students by compatibility")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            manager.review_students()

        elif choice == '2':
            manager.add_student()

        elif choice == '3':
            matcher = MatchMaker(manager.students)
            pairs = matcher.get_best_matches()

            if not pairs:
                print("No matching pairs found.")
            else:
                print("\nMatching Results:")
                for (s1, s2), score in pairs:
                    print(f"{s1['name']} <--> {s2['name']} (Score: {score})")

        elif choice == '4':
            manager.delete_student()

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
