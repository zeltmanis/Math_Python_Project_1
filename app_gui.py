import tkinter as tk
from tkinter import simpledialog, messagebox
from student_manager import StudentManager
from student_helper import StudentHelper
from matchmaker import MatchMaker

class AppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Matcher")
        self.manager = StudentManager()
        self.helper = StudentHelper()

        # Buttons for actions
        tk.Button(root, text="Review Students", command=self.review_students).pack(pady=5)
        tk.Button(root, text="Add Student", command=self.add_student).pack(pady=5)
        tk.Button(root, text="Delete Student", command=self.delete_student).pack(pady=5)
        tk.Button(root, text="Match Students", command=self.match_students).pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    def review_students(self):
        if not self.manager.students:
            messagebox.showinfo("Review Students", "No students found.")
            return

        info = "\n\n".join(self.helper.format_student(s, idx + 1) for idx, s in enumerate(self.manager.students))

        # Create a scrollable top-level window
        window = tk.Toplevel(self.root)
        window.title("Student List")
        window.geometry("500x400")  # Width x Height

        frame = tk.Frame(window)
        frame.pack(fill=tk.BOTH, expand=True)

        text_area = tk.Text(frame, wrap=tk.WORD)
        text_area.insert(tk.END, info)
        text_area.config(state=tk.DISABLED)
        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame, command=text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.config(yscrollcommand=scrollbar.set)

        # Add a close button at the bottom
        tk.Button(window, text="Close", command=window.destroy).pack(pady=5)

    def add_student(self):
        name = simpledialog.askstring("Add Student", "Enter name:")
        if not name: return

        age = simpledialog.askstring("Add Student", "Enter age:")
        if not age: return

        gender = simpledialog.askstring("Add Student", "Enter gender:")
        if not gender: return

        country = simpledialog.askstring("Add Student", "Enter country:")
        if not country: return

        sports = self.helper.ask_choice_dialog(self.root, "Select Sports", self.helper.SPORTS_OPTIONS)
        if sports is None: return

        art = self.helper.ask_choice_dialog(self.root, "Select Art", self.helper.ART_OPTIONS)
        if art is None: return

        games = self.helper.ask_choice_dialog(self.root, "Select Games", self.helper.GAMES_OPTIONS)
        if games is None: return

        movie = self.helper.ask_choice_dialog(self.root, "Select Movie", self.helper.MOVIE_OPTIONS)
        if movie is None: return

        new_student = {
            'name': name,
            'age': age,
            'gender': gender,
            'country': country,
            'sports': sports,
            'art': art,
            'games': games,
            'movie': movie
        }

        self.manager.students.append(new_student)
        self.manager.save_students()
        messagebox.showinfo("Success", f"Student '{name}' added successfully!")

    def delete_student(self):
        if not self.manager.students:
            messagebox.showinfo("Delete Student", "No students to delete.")
            return

        choices = "\n\n".join(self.format_student(s, idx+1) for idx, s in enumerate(self.manager.students))
        selected = simpledialog.askinteger("Delete Student", f"Select student to delete:\n\n{choices}")
        if selected is None:
            return
        if 1 <= selected <= len(self.manager.students):
            removed = self.manager.students.pop(selected - 1)
            self.manager.save_students()
            messagebox.showinfo("Deleted", f"Student '{removed['name']}' deleted.")
        else:
            messagebox.showerror("Error", "Invalid selection.")

    def format_student(self, student, number=None):
        prefix = f"{number}. " if number else ""
        return (f"{prefix}{student['name']} ({student['age']}), {student['gender']}, {student['country']}\n"
                f"    Sports: {student.get('sports', 'N/A')}, Art: {student.get('art', 'N/A')}, "
                f"Games: {student.get('games', 'N/A')}, Movie: {student.get('movie', 'N/A')}")

    def match_students(self):
        if len(self.manager.students) < 2:
            messagebox.showinfo("Match Students", "Not enough students to match.")
            return

        matcher = MatchMaker(self.manager.students)
        best_matches = matcher.get_best_matches()

        if not best_matches:
            messagebox.showinfo("Match Students", "No matching pairs found.")
            return

        result_lines = []
        for (s1, s2), score in best_matches:
            result_lines.append(f"{s1['name']} <--> {s2['name']} (Score: {score})")

        result_text = "\n".join(result_lines)
        messagebox.showinfo("Best Matches", result_text)

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = AppGUI(root)
    root.mainloop()