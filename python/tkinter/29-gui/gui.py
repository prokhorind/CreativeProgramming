import tkinter as tk
from tkinter import messagebox
import requests
#ngrok http --url=obliging-precisely-dove.ngrok-free.app 8000
#uvicorn main:app --reload
API_URL = "https://obliging-precisely-dove.ngrok-free.app"


class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter CRUD App")

        self.create_user_list_frame()
        self.create_form_frame()
        self.create_buttons()

        self.get_users()

    def create_user_list_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Users List").pack()
        self.user_listbox = tk.Listbox(frame)
        self.user_listbox.pack(fill=tk.BOTH, expand=True)
        tk.Button(frame, text="Refresh Users", command=self.get_users).pack()

    def create_form_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.X)

        self.name_entry = self.create_labeled_entry(frame, "Name", 0)
        self.surname_entry = self.create_labeled_entry(frame, "Surname", 1)
        self.age_entry = self.create_labeled_entry(frame, "Age", 2)
        self.user_id_entry = self.create_labeled_entry(frame, "User ID (For Update/Delete/Get)", 3)

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.X)

        actions = [
            ("Create User", self.create_user),
            ("Get User", self.get_user),
            # TODO: Додати кнопку "Update User"
            # TODO: Додати кнопку "Delete User"
        ]
        for text, command in actions:
            tk.Button(frame, text=text, command=command).pack(side=tk.LEFT, padx=5)

    def create_labeled_entry(self, frame, label, row):
        tk.Label(frame, text=label).grid(row=row, column=0)
        entry = tk.Entry(frame)
        entry.grid(row=row, column=1)
        return entry

    def api_request(self, method, endpoint, params=None):
        try:
            url = f"{API_URL}{endpoint}"
            response = requests.request(method, url, params=params)
            response.raise_for_status()
            return response.json() if response.content else None
        except requests.RequestException as e:
            messagebox.showerror("Error", f"API request failed: {e}")
            return None

    def get_users(self):
        users = self.api_request("GET", "/users/")
        if users is not None:
            self.user_listbox.delete(0, tk.END)
            for user in users:
                self.user_listbox.insert(
                    tk.END,
                    f"ID: {user['id']}, Name: {user['name']}, Surname: {user['surname']}, Age: {user['age']}",
                )

    def create_user(self):
        params = self.collect_form_data()
        if params:
            if self.api_request("POST", "/users/", params=params):
                messagebox.showinfo("Success", "User created successfully!")
                self.get_users()

    def get_user(self):
        user_id = self.user_id_entry.get()
        if user_id:
            user = self.api_request("GET", f"/users/{user_id}")
            if user:
                messagebox.showinfo("User Info", f"ID: {user['id']}, Name: {user['name']}, Surname: {user['surname']}, Age: {user['age']}")

    def collect_form_data(self):
        try:
            return {
                "name": self.name_entry.get(),
                "surname": self.surname_entry.get(),
                "age": int(self.age_entry.get()),
            }
        except ValueError:
            messagebox.showerror("Error", "Age must be an integer.")
            return None


if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()
