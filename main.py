from student_manager import StudentManager
from matchmaker import MatchMaker

def main():
    manager = StudentManager()  # Load students from CSV

    while True:
        print("\nWhat would you like to do?")
        print("1. Review students")
        print("2. Add new student")
        print("3. Match students (best matches)")
        print("4. Match students (mutual matches)")
        print("5. Delete a student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            manager.review_students()

        elif choice == '2':
            manager.add_student()

        elif choice == '3':  # Best matches
            if not manager.students or len(manager.students) < 2:
                print("Not enough students to perform matching.")
                continue
            matcher = MatchMaker(manager.students)
            best_matches = matcher.get_best_matches()
            if not best_matches:
                print("No best matches found.")
            else:
                print("\n--- Best Matches ---")
                for ((s1, s2), score) in best_matches:
                    print(f"{s1['name']} (ID {s1['id']}) <--> {s2['name']} (ID {s2['id']}) | Compatibility Score: {score}")
                print("--------------------\n")

        elif choice == '4':  # Mutual matches
            if not manager.students or len(manager.students) < 2:
                print("Not enough students to perform matching.")
                continue
            matcher = MatchMaker(manager.students)
            mutual_matches = matcher.get_mutual_matches()
            if not mutual_matches:
                print("No mutual matches found.")
            else:
                print("\n--- Mutual Matches ---")
                for ((s1, s2), score) in mutual_matches:
                    print(f"{s1['name']} (ID {s1['id']}) <--> {s2['name']} (ID {s2['id']}) | Average Compatibility Score: {score}")
                print("----------------------\n")

        elif choice == '5':
            manager.delete_student()

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()