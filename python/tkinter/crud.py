import tkinter as tk
from tkinter import messagebox, simpledialog
import requests

# Constants
BASE_URL = 'https://jsonplaceholder.typicode.com/posts'

# Functions
def fetch_posts():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        posts = response.json()
        text_output.delete(1.0, tk.END)
        for post in posts:
            text_output.insert(tk.END, f"ID: {post['id']}\nTitle: {post['title']}\nBody: {post['body']}\n\n")
    except requests.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def create_post():
    title = simpledialog.askstring("Input", "Enter the title:")
    body = simpledialog.askstring("Input", "Enter the body:")
    if title and body:
        try:
            response = requests.post(BASE_URL, json={"title": title, "body": body, "userId": 1})
            response.raise_for_status()
            messagebox.showinfo("Success", "Post created successfully!")
            fetch_posts()
        except requests.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def update_post():
    post_id = simpledialog.askinteger("Input", "Enter the ID of the post to update:")
    title = simpledialog.askstring("Input", "Enter the new title:")
    body = simpledialog.askstring("Input", "Enter the new body:")
    if post_id and title and body:
        try:
            response = requests.put(f"{BASE_URL}/{post_id}", json={"title": title, "body": body, "userId": 1})
            response.raise_for_status()
            messagebox.showinfo("Success", "Post updated successfully!")
            fetch_posts()
        except requests.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def delete_post():
    post_id = simpledialog.askinteger("Input", "Enter the ID of the post to delete:")
    if post_id:
        try:
            response = requests.delete(f"{BASE_URL}/{post_id}")
            response.raise_for_status()
            messagebox.showinfo("Success", "Post deleted successfully!")
            fetch_posts()
        except requests.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# GUI
root = tk.Tk()
root.title("CRUD App with Tkinter")

frame = tk.Frame(root)
frame.pack(pady=10)

fetch_button = tk.Button(frame, text="Fetch Posts", command=fetch_posts)
fetch_button.pack(side=tk.LEFT, padx=5)

create_button = tk.Button(frame, text="Create Post", command=create_post)
create_button.pack(side=tk.LEFT, padx=5)

update_button = tk.Button(frame, text="Update Post", command=update_post)
update_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(frame, text="Delete Post", command=delete_post)
delete_button.pack(side=tk.LEFT, padx=5)

text_output = tk.Text(root, height=20, width=80)
text_output.pack(pady=10)

root.mainloop()