from tkinter import simpledialog, messagebox

class StudentHelper:
    SPORTS_OPTIONS = ["ball sports", "winter sports", "martial arts", "other", "none"]
    ART_OPTIONS = ["painting", "dancing", "singing", "other", "none"]
    GAMES_OPTIONS = ["FPS games", "Strategy games", "RPG games", "other", "none"]
    MOVIE_OPTIONS = ["horror", "drama", "action", "comedy", "sci-fi", "none"]

    def ask_choice_dialog(self, root, title, options):
        options_str = "\n".join(f"{i+1}. {option}" for i, option in enumerate(options))
        while True:
            choice = simpledialog.askstring(title, f"{options_str}\nEnter number:")
            if choice is None:
                return None
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                return options[int(choice) - 1]
            else:
                messagebox.showerror("Invalid", "Please enter a valid number.")