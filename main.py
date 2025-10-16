from student_manager import StudentManager
from matchmaker import MatchMaker

def main():
    manager = StudentManager()  # Initialize StudentManager, loads students from CSV

    while True:
        # Display menu options to the user
        print("\nWhat would you like to do?")
        print("1. Review students")
        print("2. Add new student")
        print("3. Match students (one-way matches)")
        print("4. Match students (mutual symmetric matches)")
        print("5. Match students (transitive matches)")
        print("6. Delete a student")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            # Show list of all students
            manager.review_students()

        elif choice == '2':
            # Add a new student to the system
            manager.add_student()

        elif choice == '3':  # One-way (best) matches
            # Require at least 2 students to perform matching
            if len(manager.students) < 2:
                print("Not enough students to perform matching.")
                continue

            matcher = MatchMaker(manager.students)
            best_matches = matcher.get_best_matches()  # Get one-way compatibility matches

            if not best_matches:
                print("No one-way matches found.")
            else:
                print("\n--- One-way Matches ---")
                # Display matches with directional arrow and compatibility score
                for ((s1, s2), score) in best_matches:
                    print(f"{s1['name']} (ID {s1['id']}) → {s2['name']} (ID {s2['id']}) | Compatibility Score: {score}")
                print("------------------------\n")

        elif choice == '4':  # Symmetric (mutual) matches
            # Require at least 2 students to perform matching
            if len(manager.students) < 2:
                print("Not enough students to perform matching.")
                continue

            matcher = MatchMaker(manager.students)
            symmetric_matches = matcher.get_symmetric_matches()  # Get mutual matches where both students score each other

            if not symmetric_matches:
                print("No symmetric matches found.")
            else:
                print("\n--- Mutual Symmetric Matches ---")
                # Display mutual matches with double-headed arrow and average compatibility score
                for ((s1, s2), score) in symmetric_matches:
                    print(f"{s1['name']} (ID {s1['id']}) ⇄ {s2['name']} (ID {s2['id']}) | Avg Compatibility Score: {score}")
                print("----------------------------------\n")

        elif choice == '5':  # Transitive matches
            # Require at least 3 students to perform matching
            if len(manager.students) < 3:
                print("Not enough students to perform matching.")
                continue

            matcher = MatchMaker(manager.students)
            transitive_matches = matcher.get_transitive_matches()  # Find transitive connections (a connected to c via b)

            if not transitive_matches:
                print("No transitive matches found.")
            else:
                print("\n--- Transitive Matches ---")
                # Show transitive matches indicating the intermediate student connecting them
                for (a, c, b) in transitive_matches:
                    print(f"{a['name']} (ID {a['id']}) ⇄ {c['name']} (ID {c['id']}) — via {b['name']} (ID {b['id']})")
                print("----------------------------\n")

        elif choice == '6':
            # Delete a student from the system
            manager.delete_student()

        elif choice == '7':
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid input
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
