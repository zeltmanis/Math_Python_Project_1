import tkinter as tk
from tkinter import messagebox, simpledialog
from student_manager import StudentManager
from matchmaker import Matchmaker

class StudentApp:
    def __init__(self, root):
        self.manager = StudentManager()
        self.root = root
        self.root.title("Student Matching System")

        # Buttons
        tk.Button(root, text="Review Students", width=30, command=self.review_students).pack(pady=5)
        tk.Button(root, text="Add Student", width=30, command=self.add_student).pack(pady=5)
        tk.Button(root, text="Delete Student", width=30, command=self.delete_student).pack(pady=5)
        tk.Button(root, text="Match Students", width=30, command=self.match_students).pack(pady=5)
        tk.Button(root, text="Exit", width=30, command=root.quit).pack(pady=5)

    def review_students(self):
        students = self.manager.students
        if not students:
            messagebox.showinfo("Students", "No students to show.")
            return
        info = "\n".join(
            f"{i+1}. {s['name']} ({s['age']}), {s['gender']}, {s['country']}"
            for i, s in enumerate(students)
        )
        messagebox.showinfo("Student List", info)

    def add_student(self):
        name = simpledialog.askstring("Add Student", "Enter name:")
        if not name: return
        age = simpledialog.askstring("Add Student", "Enter age:")
        if not age: return
        gender = simpledialog.askstring("Add Student", "Enter gender:")
        if not gender: return
        country = simpledialog.askstring("Add Student", "Enter country:")
        if not country: return

        self.manager.students.append({
            'name': name,
            'age': age,
            'gender': gender,
            'country': country
        })
        self.manager.save_students()
        messagebox.showinfo("Success", f"{name} was added.")

    def delete_student(self):
        students = self.manager.students
        if not students:
            messagebox.showinfo("Delete Student", "No students to delete.")
            return

        choices = "\n".join(
            f"{i+1}. {s['name']} ({s['age']}, {s['country']})"
            for i, s in enumerate(students)
        )
        num = simpledialog.askinteger("Delete Student", f"Enter number to delete:\n\n{choices}")
        if not num or num < 1 or num > len(students):
            messagebox.showerror("Error", "Invalid selection.")
            return

        removed = students.pop(num - 1)
        self.manager.save_students()
        messagebox.showinfo("Deleted", f"{removed['name']} was deleted.")

    def match_students(self):
        matcher = Matchmaker(self.manager.students)
        matches = matcher.get_matches()
        if matches:
            result = "\n".join(f"{a} & {b}" for a, b in matches)
        else:
            result = "No compatible matches found."
        messagebox.showinfo("Matches", result)

# You run this file directly
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()