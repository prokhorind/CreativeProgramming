import tkinter as tk

def show_status():
    label.config(text=f"Checked: {var.get()}")

# Create the main window
root = tk.Tk()
root.title("Checkbox Example")

# Create a checkbox
var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Check me", variable=var, command=show_status)
checkbox.pack()

# Label to show the checkbox status
label = tk.Label(root, text="Checked: False")
label.pack()

# Start the GUI event loop
root.mainloop()