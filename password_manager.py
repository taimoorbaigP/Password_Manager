import tkinter as tk
from tkinter import messagebox, simpledialog
import json
from ttkthemes import ThemedTk

PASSWORDS_FILE = "passwords.json"

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")

        self.passwords = self.load_passwords()

        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)
        self.menu_bar.add_command(label="Add Password", command=self.add_password)
        self.menu_bar.add_command(label="View Passwords", command=self.view_passwords)


    def load_passwords(self):
        try:
            with open(PASSWORDS_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_passwords(self):
        with open(PASSWORDS_FILE, "w") as file:
            json.dump(self.passwords, file)

    def add_password(self):
        website = simpledialog.askstring("Add Password", "Enter website:")
        password = simpledialog.askstring("Add Password", f"Enter password for {website}:")

        if website and password:
            self.passwords[website] = password
            self.save_passwords()
            messagebox.showinfo("Success", "Password added successfully!")
        else:
            messagebox.showwarning("Error", "Website and password are required.")

    def view_passwords(self):
        if self.passwords:
            passwords_window = tk.Toplevel(self.root)
            passwords_window.title("View Passwords")

            text_widget = tk.Text(passwords_window)
            text_widget.pack()

            for website, password in self.passwords.items():
                text_widget.insert(tk.END, f"Website: {website}\nPassword: {password}\n\n")

            text_widget.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Info", "No passwords stored yet.")

def main():
    root = ThemedTk(theme="dark")  # You can experiment with different themes
    app = PasswordManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()